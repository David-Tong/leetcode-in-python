class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.anses = []

        def doCalculate(numbers):
            stack = []
            for item in numbers:
                if item == "+" or item == "-" or item == "*":
                    number2 = stack.pop()
                    number = stack.pop()
                    if item == "+":
                        stack.append(number + number2)
                    elif item == "-":
                        stack.append(number - number2)
                    elif item == "*":
                        stack.append(number * number2)
                else:
                    stack.append(item)
            return stack[0]

        def doOperate(num, target, expr, action, numbers, operators):
            # stop recursion
            if len(num) == 0:
                while operators:
                    numbers.append(operators.pop())
                # print(numbers)
                if doCalculate(numbers) == target:
                    self.anses.append(expr)
                return

            # add operator
            if action == "Operator":
                for operator in ("+", "-", "*"):
                    tmp_numbers = numbers[:]
                    tmp_operators = operators[:]
                    if operator == "+" or operator == "-":
                        while tmp_operators:
                            tmp_numbers.append(tmp_operators.pop())
                    tmp_operators.append(operator)
                    doOperate(num[:], target, expr + operator, "Number", tmp_numbers[:], tmp_operators[:])
            # add numbers
            elif action == "Number":
                for x in range(len(num)):
                    number = num[:x + 1]
                    # filter all number like "0xxx"
                    if number[0] == "0" and len(number) > 1:
                        continue
                    doOperate(num[x + 1:], target, expr + number, "Operator", numbers[:] + [int(number)], operators[:])

        doOperate(num, target, "", "Number", [], [])
        return self.anses


num = "123"
target = 6

num = "232"
target = 8

num = "3456237490"
target = 9191

num = "105"
target = 5

num = "1000000009"
target = 9

num = "0000"
target = 0

num = "2147483647"
target = 2147483647

num = "2147483647"
target = -2147483647

num = "010"
target = 0

num = "00"
target = 0

solution = Solution()
print(solution.addOperators(num, target))
