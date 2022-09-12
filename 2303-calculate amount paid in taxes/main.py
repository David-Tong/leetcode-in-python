class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        tax = 0
        brackets = [[0, 0]] + brackets
        for idx in range(len(brackets)):
            if idx > 0:
                prev = brackets[idx - 1]
                curr = brackets[idx]
                if curr[0] > income:
                    tax += (income - prev[0]) * curr[1] / 100.0
                    break
                else:
                    tax += (curr[0] - prev[0]) * curr[1] / 100.0
        return tax


brackets = [[3,50],[7,10],[12,25]]
income = 10

"""
brackets = [[1,0],[4,25],[5,50]]
income = 2

brackets = [[2,50]]
income = 0
"""

solution = Solution()
print(solution.calculateTax(brackets, income))
