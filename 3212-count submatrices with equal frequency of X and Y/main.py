class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        xs = [[0] * N for _ in range(M)]
        ys = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if y == 0:
                    if grid[x][y] == "X":
                        xs[x][y] = 1
                    if grid[x][y] == "Y":
                        ys[x][y] = 1
                else:
                    if grid[x][y] == "X":
                        xs[x][y] = xs[x][y - 1] + 1
                    else:
                        xs[x][y] = xs[x][y - 1]
                    if grid[x][y] == "Y":
                        ys[x][y] = ys[x][y - 1] + 1
                    else:
                        ys[x][y] = ys[x][y - 1]

        for x in range(M):
            for y in range(N):
                if x > 0:
                    xs[x][y] += xs[x - 1][y]
                    ys[x][y] += ys[x - 1][y]

        # print(xs)
        # print(ys)

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                if xs[x][y] > 0:
                    if xs[x][y] == ys[x][y]:
                        ans += 1
        return ans


grid = [["X","Y","."],["Y",".","."]]
grid = [["X","X"],["X","Y"]]
grid = [[".","."],[".","."]]

import random
grid = [[random.choice(["X", "Y", "."]) for _ in range(100)] for _ in range(100)]
print(grid)

solution = Solution()
print(solution.numberOfSubmatrices(grid))
