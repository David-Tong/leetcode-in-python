class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def getConnectedLands(x, y):
            connected = 0
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if grid[nx][ny] == 1:
                        connected += 1
            return connected


        M = len(grid)
        N = len(grid[0])
        lands = 0
        connecteds = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    lands += 1
                    connecteds += getConnectedLands(x, y)

        ans = lands * 4 - connecteds
        return ans


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1]]
grid = [[1,0]]
grid = [[1,1],[1,1]]

solution = Solution()
print(solution.islandPerimeter(grid))
