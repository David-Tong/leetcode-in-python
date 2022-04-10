class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.dp = [[0] * self.N for x in range(self.M)]
        for x in range(self.M):
            for y in range(self.N):
                if y > 0:
                    self.dp[x][y] = self.dp[x][y-1] + matrix[x][y]
                else:
                    self.dp[x][y] = matrix[x][y]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                ans += self.dp[row][col2] - self.dp[row][col1 - 1]
            else:
                ans += self.dp[row][col2]
        return ans


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))
