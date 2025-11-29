class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        # process
        stack = list()
        operators = ['*', '/', '+', '-']

        idx = 0
        stack.append(n - idx)
        idx += 1
        while idx < n:
            mod = (idx - 1) % 4
            operator = operators[mod]
            operand2 = n - idx
            if operator == "*":
                operand = stack.pop()
                stack.append(operand * operand2)
            elif operator == "/":
                operand = stack.pop()
                if operand < 0:
                    stack.append(-1 * ((-1 * operand) // operand2))
                else:
                    stack.append(operand // operand2)
            elif operator == "+":
                stack.append(operand2)
            elif operator == "-":
                stack.append(-1 * operand2)
            else:
                raise Exception
            idx += 1

        # post-process
        ans = 0
        while stack:
            ans += stack.pop()
        return ans


n = 4
n = 10
n = 12

solution = Solution()
print(solution.clumsy(n))
