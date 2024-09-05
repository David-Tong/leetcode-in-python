class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        # process rows
        for x in range(M):
            if grid[x][0] == 0:
                for y in range(N):
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    else:
                        grid[x][y] = 0

        # process columns
        for y in range(1, N):
            total = 0
            for x in range(M):
                total += grid[x][y]
            if total <= M // 2:
                for x in range(M):
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    else:
                        grid[x][y] = 0

        # calculate
        ans = 0
        for y in range(N):
            total = 0
            for x in range(M):
                total += grid[x][y]
            ans += total * 2 ** (N - 1 - y)
        return ans


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
grid = [[0]]
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0],[0,0,0,1],[1,0,0,1]]

solution = Solution()
print(solution.matrixScore(grid))
