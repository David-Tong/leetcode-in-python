class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(("", -1))
        ans = 0
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(("(", idx))
            elif ch == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                    ans = max(ans, idx - stack[-1][1])
                else:
                    stack.append((")", idx))
        return ans


s = "(()"
s = "(())"
s = ")()())"
s = "(())(()())"
s = ")))(())(()"
#s = ""

solution = Solution()
print(solution.longestValidParentheses(s))
