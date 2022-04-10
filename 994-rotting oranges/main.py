class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isValid(grid, x, y):
            if x < 0 or x >= len(grid) or \
                y < 0 or y >= len(grid[0]):
                return False

            if grid[x][y] == 0 or grid[x][y] == 2:
                return False

            return True

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        from collections import deque

        bfs = deque()
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfs.append((i, j))

        if len(bfs) > 0:
            ans = -1

        while len(bfs) > 0:
            size = len(bfs)
            ans += 1
            for i in range(size):
                x, y = bfs.popleft()
                for delta_x, delta_y in DIRECTIONS:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if isValid(grid, next_x, next_y):
                        grid[next_x][next_y] = 2
                        bfs.append((next_x, next_y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = -1

        return ans


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
#grid = [[0]]

solution = Solution()
print(solution.orangesRotting(grid))
