class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif ch == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif ch == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


s = "()"
#s = "()[]{}"
s = "(]"
#s = "("

solution = Solution()
print(solution.isValid(s))
