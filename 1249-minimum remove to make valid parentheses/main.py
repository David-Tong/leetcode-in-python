class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        parentheses = 0

        for ch in s:
            if ch == "(":
                stack.append(ch)
                parentheses += 1
            elif ch == ")":
                if parentheses > 0:
                    parentheses -= 1
                    stack.append(ch)
            else:
                stack.append(ch)

        ans = ""
        for ch in stack[::-1]:
            if parentheses > 0 and ch == "(":
                parentheses -= 1
            else:
                ans = ch + ans
        return ans


s = "lee(t(c)o)de)"
s = "a)b(c)d"
s = "))(("
s = "a)b(cd(cd"

solution = Solution()
print(solution.minRemoveToMakeValid(s))
