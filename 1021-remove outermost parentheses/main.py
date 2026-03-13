class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # process
        ans = ""
        count = 0
        for ch in s:
            if ch == "(":
                count += 1
                if count == 1:
                    pass
                else:
                    ans += ch
            elif ch == ")":
                count -= 1
                if count == 0:
                    pass
                else:
                    ans += ch
        return ans


s = "(()())(())"
s = "(()())(())(()(()))"
s = "()()"

solution = Solution()
print(solution.removeOuterParentheses(s))
