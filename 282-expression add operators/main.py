class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.N = len(num)
        self.anses = []

        def backtrack(expr, i, res, mul):
            if i == self.N:
                if res == target:
                    self.anses.append("".join(expr))
                return

            # index for operator
            idx = len(expr)

            if i > 0:
                expr.append("")

            # enumerate numbers
            val = 0
            for j in range(i, self.N):
                # can't have a number like "0X"
                if j > i and num[i] == "0":
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])

                # can't add an operator at the beginning of expression
                if i == 0:
                    backtrack(expr, j + 1, val, val)
                else:
                    # enumerate operators
                    expr[idx] = "+";
                    backtrack(expr, j + 1, res + val, val)
                    expr[idx] = "-";
                    backtrack(expr, j+1, res - val, -1 * val)
                    expr[idx] = "*";
                    backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[idx:]

        backtrack([], 0, 0, 0)
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
