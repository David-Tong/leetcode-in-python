class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        rows = [0] * M
        cols = [0] * N
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    rows[x] += 1
                    cols[y] += 1

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    ans += (rows[x] - 1) * (cols[y] - 1)
        return ans


grid = [[0,1,0],[0,1,1],[0,1,0]]
grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
grid = [[1,0,1],[1,0,0],[1,0,0]]

from random import randint
grid = [[randint(0, 1) for _ in range(500)] for _ in range(500)]
print(grid)

solution = Solution()
print(solution.numberOfRightTriangles(grid))
