class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        # pre-process
        L = len(s)

        def add(s):
            digits = [""] * L
            for x in range(L):
                if x % 2 == 0:
                    digits[x] = s[x]
                else:
                    digits[x] = str((int(s[x]) + int(a)) % 10)
            return "".join(digits)

        def rotate(s):
            return s[L - b:] + s[: L - b]

        # bfs
        from collections import deque
        bfs = deque()
        from collections import defaultdict
        visited = defaultdict(bool)

        bfs.append(s)
        visited[s] = True

        ans = "9" * L
        while bfs:
            curr = bfs.popleft()
            ans = min(ans, curr)
            # add
            nxt = add(curr)
            if not nxt in visited:
                bfs.append(nxt)
                visited[nxt] = True
            # rotate
            nxt = rotate(curr)
            if not nxt in visited:
                bfs.append(nxt)
                visited[nxt] = True
        return ans


s = "5525"
a = 9
b = 2

s = "74"
a = 5
b = 1

s = "0011"
a = 4
b = 2

solution = Solution()
print(solution.findLexSmallestString(s, a, b))
