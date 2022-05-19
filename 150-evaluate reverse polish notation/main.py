class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                oper2 = stack.pop()
                oper = stack.pop()
                if token == "+":
                    stack.append(oper + oper2)
                elif token == "-":
                    stack.append(oper - oper2)
                elif token == "*":
                    stack.append(oper * oper2)
                elif token == "/":
                    stack.append(int(oper * 1.0 / oper2))
            else:
                stack.append(int(token))
        return stack[-1]


tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

solution = Solution()
print(solution.evalRPN(tokens))
