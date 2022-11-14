class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        def sum_of_hourglass(grid, x, y):
            return grid[x][y] + grid[x][y + 1] + grid[x][y + 2] \
                        + grid[x + 1][y + 1] \
                        + grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]

        ans = 0
        for x in range(M - 2):
            for y in range(N - 2):
                ans = max(ans, sum_of_hourglass(grid, x, y))
        return ans


grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
grid = [[1,2,3],[4,5,6],[7,8,9]]

solution = Solution()
print(solution.maxSum(grid))
