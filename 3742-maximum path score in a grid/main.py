class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # process
        # dp init
        # dp[x][y][z] = max path score at grid[x][y] with z cost remained
        from collections import defaultdict
        dp = [[defaultdict() for _ in range(N)] for _ in range(M)]
        dp[0][0][k] = grid[0][0]

        # dp transfer
        for x in range(M):
            for y in range(N):
                if x > 0:
                    for z in dp[x - 1][y]:
                        if grid[x][y] == 0:
                            if z not in dp[x][y]:
                                dp[x][y][z] = dp[x - 1][y][z]
                            else:
                                dp[x][y][z] += max(dp[x][y][z], dp[x - 1][y][z])
                        else:
                            if z > 0:
                                if z - 1 not in dp[x][y]:
                                    dp[x][y][z - 1] = dp[x - 1][y][z] + grid[x][y]
                                else:
                                    dp[x][y][z - 1] = max(dp[x][y][z - 1], dp[x - 1][y][z] + grid[x][y])
                if y > 0:
                    for z in dp[x][y - 1]:
                        if grid[x][y] == 0:
                            if z not in dp[x][y]:
                                dp[x][y][z] = dp[x][y - 1][z]
                            else:
                                dp[x][y][z] = max(dp[x][y][z], dp[x][y - 1][z])
                        else:
                            if z > 0:
                                if z - 1 not in dp[x][y]:
                                    dp[x][y][z - 1] = dp[x][y - 1][z] + grid[x][y]
                                else:
                                    dp[x][y][z - 1] = max(dp[x][y][z - 1], dp[x][y - 1][z] + grid[x][y])

        # print(dp)
        if len(dp[M - 1][N - 1]) > 0:
            return max(dp[M - 1][N - 1].values())
        else:
            return -1


grid = [[0, 1],[2, 0]]
k = 1

grid = [[0, 1],[1, 2]]
k = 1

from random import randint
grid = [[randint(0,2) for _ in range(200)] for _ in range(200)]
grid[0][0] = 0
k = 500
print(grid)

solution = Solution()
print(solution.maxPathScore(grid, k))
