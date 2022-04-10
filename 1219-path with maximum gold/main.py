class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global ans
        ans = 0
        gold = 0

        def dfs(x, y, grid, gold):
            if x < 0 or x >= len(grid) or \
                y < 0 or y >= len(grid[0]) or \
                    grid[x][y] == 0:
                return
            else:
                global ans
                tmp = grid[x][y]
                ans = max(ans, gold + tmp)
                grid[x][y] = 0
                dfs(x - 1, y, grid, gold + tmp)
                dfs(x + 1, y, grid, gold + tmp)
                dfs(x, y - 1, grid, gold + tmp)
                dfs(x, y + 1, grid, gold + tmp)
                grid[x][y] = tmp

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                dfs(x, y, grid, gold)

        return ans


solution = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
grid = [[1]]
print(solution.getMaximumGold(grid))

