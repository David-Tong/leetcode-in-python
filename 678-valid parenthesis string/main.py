class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process
        stack = list()
        for ch in s:
            if ch == "(" or ch == "*":
                stack.append(ch)
            elif ch == ")":
                if stack:
                    has = False
                    for x in range(len(stack) - 1, -1, -1):
                        if stack[x] == "(":
                            stack.pop(x)
                            has = True
                            break
                    if not has:
                        stack.pop()
                else:
                    return False

        # post process
        post_stack = list()
        for ch in stack:
            if ch == "(":
                post_stack.append(ch)
            elif ch == "*":
                if post_stack:
                    post_stack.pop()

        if post_stack:
            return False
        else:
            return True


s = "()"
s = "(*)"
s = "(*))"
s = "())*)"
s = "()()())"
s = "((**))"
s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

solution = Solution()
print(solution.checkValidString(s))
