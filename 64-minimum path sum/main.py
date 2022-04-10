class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for x in range(M)]

        for x in range(M):
            for y in range(N):
                dp[x][y] = grid[x][y]
                if x > 0 and y > 0:
                    dp[x][y] += min(dp[x - 1][y], dp[x][y-1])
                    continue
                if x > 0:
                    dp[x][y] += dp[x-1][y]
                if y > 0:
                    dp[x][y] += dp[x][y-1]
        return dp[M-1][N-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid = [[1, 2, 3], [4, 5, 6]]

solution = Solution()
print(solution.minPathSum(grid))
