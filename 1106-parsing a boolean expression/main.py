class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = list()
        for ch in expression:
            if ch == ")":
                temp = list()
                while stack[-1] != "(":
                    temp.append(stack.pop())
                # pop "("
                stack.pop()
                # pop operator of "!", "&", "|"
                operator = stack.pop()
                if operator == "!":
                    res = not temp[0]
                elif operator == "&":
                    res = True
                    for item in temp:
                        res = res and item
                elif operator == "|":
                    res = False
                    for item in temp:
                        res = res or item
                else:
                    raise ValueError
                stack.append(res)
            else:
                if ch == "f":
                    stack.append(False)
                elif ch == "t":
                    stack.append(True)
                elif ch == ",":
                    pass
                else:
                    stack.append(ch)

        ans = stack[0]
        return ans


expression = "&(|(f))"
expression = "|(f,f,f,t)"
expression = "!(&(f,t))"
expression = "|(&(f,t,f),|(f,f,f),&(f,t,t,&(f,f,|(t,t))))"

solution = Solution()
print(solution.parseBoolExpr(expression))
