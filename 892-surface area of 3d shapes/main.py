class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] > 0:
                    ans += 2
                for delta_x, delta_y in DIRECTIONS:
                    shift_x = x + delta_x
                    shift_y = y + delta_y
                    if 0 <= shift_x < M and 0 <= shift_y < N:
                        if grid[x][y] > grid[shift_x][shift_y]:
                            ans += grid[x][y] - grid[shift_x][shift_y]
                    else:
                        ans += grid[x][y]
        return ans


grid = [[1,2],[3,4]]
grid = [[1,1,1],[1,0,1],[1,1,1]]
grid = [[2,2,2],[2,1,2],[2,2,2]]
grid = [[2,2,2],[2,2,2],[2,2,2]]

solution = Solution()
print(solution.surfaceArea(grid))
