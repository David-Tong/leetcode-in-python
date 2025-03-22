class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        rows = list()
        for row in grid:
            if sum(row) > 1:
                rows.append(True)
            else:
                rows.append(False)

        columns = list()
        for col in range(N):
            total = 0
            for row in range(M):
                total += grid[row][col]
            if total > 1:
                columns.append(True)
            else:
                columns.append(False)

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if rows[x] or columns[y]:
                        ans += 1
        return ans


grid = [[1,0],[0,1]]
grid = [[1,0],[1,1]]
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
grid = [[1]]
grid = [[1,0,0,0,0,0],[1,0,0,0,0,0],[0,1,1,1,1,1],[0,0,0,0,0,0]]

solution = Solution()
print(solution.countServers(grid))
