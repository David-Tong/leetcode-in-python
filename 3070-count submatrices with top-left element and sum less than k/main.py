class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        dp = [[0] * N for _ in range(M)]

        # process
        for x in range(M):
            for y in range(N):
                if y == 0:
                    dp[x][y] = grid[x][y]
                else:
                    dp[x][y] = dp[x][y - 1] + grid[x][y]

        ans = 0
        for x in range(M):
            for y in range(N):
                if x > 0:
                    dp[x][y] = dp[x - 1][y] + dp[x][y]
                if dp[x][y] <= k:
                    ans += 1
        return ans


grid = [[7,6,3],[6,6,1]]
k = 18

grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20

solution = Solution()
print(solution.countSubmatrices(grid, k))
