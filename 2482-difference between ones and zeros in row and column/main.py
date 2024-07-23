class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        rows = list()
        for row in grid:
            rows.append(sum(row))

        columns = list()
        for y in range(N):
            column = 0
            for x in range(M):
                column += grid[x][y]
            columns.append(column)

        # process
        ans = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                ans[x][y] = rows[x] + columns[y] - (M - rows[x]) - (N - columns[y])
        return ans


grid = [[0,1,1],[1,0,1],[0,0,1]]
grid = [[1,1,1],[1,1,1]]

solution = Solution()
print(solution.onesMinusZeros(grid))
