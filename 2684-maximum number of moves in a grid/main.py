class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp init
        M = len(grid)
        N = len(grid[0])
        dp = [[False] * N for _ in range(M)]
        for x in range(M):
            dp[x][0] = True

        # dp transfer
        ans = 0
        for y in range(1, N):
            for x in range(M):
                if x > 0 and grid[x - 1][y - 1] < grid[x][y]:
                    if dp[x - 1][y - 1]:
                        dp[x][y] |= True
                if grid[x][y - 1] < grid[x][y]:
                    if dp[x][y - 1]:
                        dp[x][y] |= True
                if x < M - 1 and grid[x + 1][y - 1] < grid[x][y]:
                    if dp[x + 1][y - 1]:
                        dp[x][y] |= True

            # check stop condition
            can = False
            for x in range(M):
                can |= dp[x][y]
            if not can:
                # print(dp)
                return ans
            ans += 1

        # print(dp)
        return ans


grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid = [[3,2,4],[2,1,9],[1,1,7]]
grid = [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]]

solution = Solution()
print(solution.maxMoves(grid))
