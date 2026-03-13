class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        cells = list()
        for x in range(M):
            for y in range(N):
                cells.append((grid[x][y], x, y))
        cells = sorted(cells, key=lambda x: (x[0], x[1], x[2]), reverse=True)
        L = len(cells)
        # print(cells)

        # process
        # dp init
        # dp[x][y] - the minimum cost to reach grid[x][y] after the k teleportation
        dp = [[float("inf")] * N for _ in range(M)]
        dp[0][0] = 0


        # dp transfer
        for z in range(k + 1):
            if z > 0:
                # case 1 - teleportation
                # dp[x][y] - min(dp[ox][oy]) where grid[ox][oy] <= grid[x][y]
                idx, idx2 = 0, 0
                mini = float("inf")
                while idx < L:
                    while idx2 < L and grid[cells[idx][1]][cells[idx][2]] <= grid[cells[idx2][1]][cells[idx2][2]]:
                        mini = min(mini, dp[cells[idx2][1]][cells[idx2][2]])
                        idx2 += 1
                    dp[cells[idx][1]][cells[idx][2]] = min(dp[cells[idx][1]][cells[idx][2]], mini)
                    idx += 1
                # print(dp)

            # case 2 - normal move
            for x in range(M):
                for y in range(N):
                    if x > 0:
                        dp[x][y] = min(dp[x][y], dp[x - 1][y] + grid[x][y])
                    if y > 0:
                        dp[x][y] = min(dp[x][y], dp[x][y - 1] + grid[x][y])
            # print(dp)

        ans = dp[M - 1][N - 1]
        return ans


grid = [[1,3,3],[2,5,4],[4,3,5]]
k = 2

grid = [[1,2],[2,3],[3,4]]
k = 1

"""
from random import randint
grid = [[randint(0, 10 ** 4) for _ in range(80)] for _ in range(80)]
grid[0][0] = 0
k = 10
print(grid)
"""

grid = [[20,26,22,25,26],[39,18,11,41,49]]
k = 1

solution = Solution()
print(solution.minCost(grid, k))
