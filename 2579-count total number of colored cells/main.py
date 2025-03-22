class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            return 4 * (n - 1) * n // 2 + 1


n = 1
n = 2
n = 3

solution = Solution()
print(solution.coloredCells(n))
