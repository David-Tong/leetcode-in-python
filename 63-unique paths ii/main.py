class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[0] * N for x in range(M)]

        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
            for x in range(M):
                for y in range(N):
                    if obstacleGrid[x][y] != 1:
                        if x > 0:
                            dp[x][y] += dp[x-1][y]
                        if y > 0:
                            dp[x][y] += dp[x][y-1]

        return dp[M-1][N-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid = [[0, 1], [0, 0]]
obstacleGrid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))

