class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def arithmetic(operator, operand, operand2):
            if operator == "+":
                return operand + operand2
            elif operator == "-":
                return operand - operand2
            elif operator == "*":
                return operand * operand2
            elif operator == "/":
                return operand // operand2

        L = len(s)

        operators = list()
        operands = list()

        number = ""
        index = 0
        while index < L:
            ch = s[index]

            # process operands
            if ord('0') <= ord(ch) <= ord('9'):
                number += ch
            else:
                if len(number) > 0:
                    operands.append(int(number))
                    number = ""

            # process operators
            if ch == "+" or ch == "-":
                while operators:
                    operand2 = operands.pop()
                    operand = operands.pop()
                    operator = operators.pop()
                    result = arithmetic(operator, operand, operand2)
                    operands.append(result)
                operators.append(ch)
            elif ch == "*" or ch == "/":
                while operators and (operators[-1] == "*" or operators[-1] == "/"):
                    operand2 = operands.pop()
                    operand = operands.pop()
                    operator = operators.pop()
                    result = arithmetic(operator, operand, operand2)
                    operands.append(result)
                operators.append(ch)

            index += 1

        # final process
        if len(number) > 0:
            operands.append(int(number))

        while operators:
            operand2 = operands.pop()
            operand = operands.pop()
            operator = operators.pop()
            result = arithmetic(operator, operand, operand2)
            operands.append(result)

        return operands[0]


s = "3+2*2"
s = " 3/2 "
s = " 3+5 / 2 "
s = "1"
s = "3 + 2 * 2 + 3 + 3 / 2"
s = "    99  "

solution = Solution()
print(solution.calculate(s))
