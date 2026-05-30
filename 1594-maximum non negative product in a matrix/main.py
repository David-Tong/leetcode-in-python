class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        MODULO = 10 ** 9 + 7

        # process
        # dp init
        maxis = [[float("-inf")] * N for _ in range(M)]
        minis = [[float("inf")] * N for _ in range(M)]
        maxis[0][0] = grid[0][0]
        minis[0][0] = grid[0][0]

        # dp transfer
        for x in range(M):
            for y in range(N):
                if x > 0:
                    maxis[x][y] = max(maxis[x][y], maxis[x - 1][y] * grid[x][y])
                    maxis[x][y] = max(maxis[x][y], minis[x - 1][y] * grid[x][y])
                    minis[x][y] = min(minis[x][y], minis[x - 1][y] * grid[x][y])
                    minis[x][y] = min(minis[x][y], maxis[x - 1][y] * grid[x][y])
                if y > 0:
                    maxis[x][y] = max(maxis[x][y], maxis[x][y - 1] * grid[x][y])
                    maxis[x][y] = max(maxis[x][y], minis[x][y - 1] * grid[x][y])
                    minis[x][y] = min(minis[x][y], minis[x][y - 1] * grid[x][y])
                    minis[x][y] = min(minis[x][y], maxis[x][y - 1] * grid[x][y])

        # dp post
        ans = max(-1, maxis[M - 1][N - 1])
        if ans > 0:
            ans = ans % MODULO
        return ans


grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
"""
grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
grid = [[1,3],[0,-4]]

from random import randint
grid = [[randint(-4, 4) for _ in range(15)] for _ in range(15)]
print(grid)
"""

solution = Solution()
print(solution.maxProductPath(grid))
