class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        # pre-process
        if equation[0] == "-":
            left_negative = True
        else:
            left_negative = False
        if equation[equation.index("=") + 1] == "-":
            right_negative = True
        else:
            right_negative = False
        if left_negative:
            equation = equation[1:]
        if right_negative:
            equation = equation[:equation.index("=") + 1] + equation[equation.index("=") + 2:]

        equation = equation + "+"
        start = 0
        flip = False
        if left_negative:
            operator = "-"
        else:
            operator = "+"
        operands = list()
        operators = list()
        for idx, ch in enumerate(equation):
            if ch == "+" or ch == "-":
                if flip:
                    if operator == "+":
                        operators.append("-")
                    else:
                        operators.append("+")
                else:
                    operators.append(operator)
                operator = ch
                operands.append(equation[start:idx])
                start = idx + 1
            elif ch == "=":
                flip = True
                operators.append(operator)
                operands.append(equation[start:idx])
                if right_negative:
                    operator = "-"
                else:
                    operator = "+"
                start = idx + 1

        #print(operators)
        #print(operands)

        # process
        coefficient = 0
        constant = 0
        for idx, operand in enumerate(operands):
            if operand[-1] == "x":
                if operators[idx] == "+":
                    if operand == "x":
                        coefficient += 1
                    else:
                        coefficient += int(operand[:-1])
                else:
                    if operand == "x":
                        coefficient -= 1
                    else:
                        coefficient -= int(operand[:-1])
            else:
                if operators[idx] == "+":
                    constant -= int(operand)
                else:
                    constant += int(operand)

        if coefficient == 0:
            if constant == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x={}".format(constant // coefficient)


equation = "x+5-3+x=6+x-2"
equation = "x=x"
equation = "2x=x"
equation = "x=x+2"
equation = "2x+3x-6x=x+2"
equation = "-x=-1"
equation = "-2x+3+7-6x=5x+2x-9-11"
equation = "2x+7+3x=-5x+9+28"

solution = Solution()
print(solution.solveEquation(equation))
