class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if len(stack) > 0:
                    if stack[-1] == "(":
                        stack.pop()
                        stack.append(1)
                    else:
                        index = len(stack) - 1
                        sumi = 0
                        while stack[-1] != "(":
                            sumi += stack[-1]
                            stack.pop()
                        stack.pop()
                        stack.append(sumi * 2)
        return sum(stack)


s = "()"
s = "(())"
s = "()()"
s = "(((()())))()"
s = "(()(()))"

solution = Solution()
print(solution.scoreOfParentheses(s))
