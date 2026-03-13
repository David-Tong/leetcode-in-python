class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # help function
        def isValid(x, y):
            blacks, whites = 0, 0
            for dx in range(2):
                for dy in range(2):
                    nx, ny = x + dx, y + dy
                    if grid[nx][ny] == 'B':
                        blacks += 1
                    elif grid[nx][ny] == 'W':
                        whites += 1
            if blacks >= 3 or whites >= 3:
                return True
            else:
                return False

        # process
        for x in range(M - 1):
            for y in range(N - 1):
                if isValid(x, y):
                    return True
        return False


grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
grid = [["B","W","B"],["B","W","W"],["B","W","W"]]

solution = Solution()
print(solution.canMakeSquare(grid))
