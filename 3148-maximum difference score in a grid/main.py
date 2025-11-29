class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp init
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for _ in range(M)]

        # dp transfer
        maxi = float("-inf")
        for x in range(M):
            for y in range(N):
                if x > 0:
                    dp[x][y] = max(dp[x][y], dp[x - 1][y] + grid[x][y] - grid[x - 1][y])
                    maxi = max(maxi, grid[x][y] - grid[x - 1][y])
                if y > 0:
                    dp[x][y] = max(dp[x][y], dp[x][y - 1] + grid[x][y] - grid[x][y - 1])
                    maxi = max(maxi, grid[x][y] - grid[x][y - 1])

        all_zeros = True
        ans = float("-inf")
        for x in range(M):
            for y in range(N):
                if dp[x][y] != 0:
                    all_zeros = False
                    ans = max(ans, dp[x][y])
        if all_zeros:
            ans = maxi
        return ans


grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
grid = [[4,3,2],[3,2,1]]

from random import randint
grid = [[randint(1, 10 ** 5) for _ in range(100)] for _ in range(100)]
print(grid)

solution = Solution()
print(solution.maxScore(grid))
