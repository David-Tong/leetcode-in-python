class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def doCompute(expression):
            operators = []
            for idx, ch in enumerate(expression):
                if ch == "+" or ch == "-" or ch == "*":
                    operators.append((idx, ch))

            results = []
            if len(operators) == 0:
                results.append(int(expression))
            elif len(operators) == 1:
                idx, operator = operators[0]
                num = int(expression[:idx])
                num2 = int(expression[idx+1:])
                if operator == "+":
                    results.append(num + num2)
                elif operator == "-":
                    results.append(num - num2)
                elif operator == "*":
                    results.append(num * num2)
            else:
                for idx, operator in operators:
                    nums = doCompute(expression[:idx])
                    nums2 = doCompute(expression[idx+1:])
                    if operator == "+":
                        for num in nums:
                            for num2 in nums2:
                                results.append(num + num2)
                    elif operator == "-":
                        for num in nums:
                            for num2 in nums2:
                                results.append(num - num2)
                    elif operator == "*":
                        for num in nums:
                            for num2 in nums2:
                                results.append(num * num2)
            return results

        return doCompute(expression)


expression = "2-1-1"
expression = "2*3-4*5"
expression = "1"
expression = "99*12+17-6"

solution = Solution()
print(solution.diffWaysToCompute(expression))
