class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        # process
        # helper functions
        # main recursive solver
        def solve( expr):
            # Case 1: no braces → literal string
            if "{" not in expr and "}" not in expr:
                return set([expr])

            # Otherwise, we must parse concatenation segments
            segments = split_segments(expr)

            # Solve each segment recursively
            results = [solve_segment(seg) for seg in segments]

            # Combine all segments by Cartesian product
            ans = results[0]
            for x in range(1, len(results)):
                ans = combine(ans, results[x])
            return ans

        # split expression into concatenation segments
        def split_segments(expr):
            res = []
            x = 0
            n = len(expr)

            while x < n:
                if expr[x] == '{':
                    # find matching }
                    y = match_brace(expr, x)
                    res.append(expr[x:y + 1])
                    x = y + 1
                else:
                    # literal letters until next brace
                    y = x
                    while y < n and expr[y] != '{':
                        y += 1
                    res.append(expr[x:y])
                    x = y
            return res

        # solve a single segment (either literal or { ... })
        def solve_segment(seg):
            if seg.startswith("{"):
                inside = seg[1:-1]
                parts = split_top_level_commas(inside)
                s = set()
                for p in parts:
                    s |= solve(p)
                return s
            else:
                return solve(seg)

        # split by commas at top level (not inside nested braces)
        def split_top_level_commas(s):
            parts = []
            start = 0
            level = 0
            for x in range(len(s)):
                if s[x] == '{':
                    level += 1
                elif s[x] == '}':
                    level -= 1
                elif s[x] == ',' and level == 0:
                    parts.append(s[start:x])
                    start = x + 1
            parts.append(s[start:])
            return parts

        # find matching } for { at position x
        def match_brace(expr, x):
            level = 0
            for y in range(x, len(expr)):
                if expr[y] == '{':
                    level += 1
                elif expr[y] == '}':
                    level -= 1
                    if level == 0:
                        return y
            return -1  # should not happen

        # cartesian product combine
        def combine(A, B):
            res = set()
            for a in A:
                for b in B:
                    res.add(a + b)
            return res

        return sorted(list(solve(expression)))


expression = "{a,b}{c,{d,e}}"
expression = "{{a,z},a{b,c},{ab,z}}"

solution = Solution()
print(solution.braceExpansionII(expression))
