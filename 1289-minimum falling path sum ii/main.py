class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        # dp[x][y] - min sum of a falling path to grid[x][y]
        dp = [[float("inf")] * N for _ in range(M)]
        for y in range(N):
            dp[0][y] = grid[0][y]

        # transfer
        for x in range(1, M):
            for y in range(N):
                for z in range(N):
                    if y != z:
                        dp[x][y] = min(dp[x][y], dp[x - 1][z])
                dp[x][y] += grid[x][y]

        print(dp)

        ans = min(dp[M - 1])
        return ans


grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[7]]
grid = [[2,3,4,5,6],[11,-5,-7,1,3],[3,4,5,-11,9],[-19,0,11,2,3],[-20,2,3,4,5]]

solution = Solution()
print(solution.minFallingPathSum(grid))
