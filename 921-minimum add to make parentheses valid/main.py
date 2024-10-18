class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()
        for ch in s:
            if ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        ans = len(stack)
        return ans


s = "())"
s = "((("
s = "(())))(()()()))))(())))"

solution = Solution()
print(solution.minAddToMakeValid(s))
