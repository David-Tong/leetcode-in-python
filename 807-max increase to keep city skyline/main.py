class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        row_maxis = list()
        for x in range(M):
            maxi = 0
            for y in range(N):
                maxi = max(maxi, grid[x][y])
            row_maxis.append(maxi)

        col_maxis = list()
        for y in range(N):
            maxi = 0
            for x in range(M):
                maxi = max(maxi, grid[x][y])
            col_maxis.append(maxi)

        # print(row_maxis)
        # print(col_maxis)

        # process
        skylines = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                skylines[x][y] = min(row_maxis[x], col_maxis[y])
        # print(skylines)

        ans = 0
        for x in range(M):
            for y in range(N):
                ans += skylines[x][y] - grid[x][y]
        return ans


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
grid = [[0,0,0],[0,0,0],[0,0,0]]

from random import randint
grid = [[randint(0, 100) for _ in range(50)] for _ in range(50)]
print(grid)

solution = Solution()
print(solution.maxIncreaseKeepingSkyline(grid))
