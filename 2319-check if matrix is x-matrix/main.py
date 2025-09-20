class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        total = 0
        for x in range(M):
            for y in range(M):
                total += grid[x][y]

        # process
        diagonals = 0
        for x in range(M):
            if grid[x][x] == 0:
                return False
            else:
                diagonals += grid[x][x]

        for x in range(M):
            if grid[x][M - 1 - x] == 0:
                return False
            else:
                diagonals += grid[x][M - 1 - x]

        if M % 2 == 1:
            diagonals -= grid[M // 2][M // 2]

        ans = diagonals == total
        return ans


grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
grid = [[5,7,0],[0,3,1],[0,5,0]]
grid = [[2,0,0,1],[0,3,0,0],[0,5,2,0],[4,0,0,2]]
grid = [[2,0,0,0,1],[0,4,0,1,5],[0,0,5,0,0],[0,5,0,2,0],[4,0,0,0,2]]

solution = Solution()
print(solution.checkXMatrix(grid))
