class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def countAreaofIsland(grid, x, y):
            def isValid(grid, x, y):
                if x < 0 or x >= len(grid) \
                    or y < 0 or y >= len(grid[0]):
                    return False
                else:
                    if grid[x][y] == 0:
                        return False
                    else:
                        return True

            from collections import deque
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            ans = 0
            if isValid(grid, x, y):
                visited = []
                bfs = deque()
                bfs.append((x, y))
                visited.append((x, y))
                while len(bfs) > 0:
                    (x, y) = bfs.popleft()
                    grid[x][y] = 0
                    ans += 1
                    for (delta_x, delta_y) in directions:
                        next_x = x + delta_x
                        next_y = y + delta_y
                        if (next_x, next_y) not in visited:
                            if isValid(grid, next_x, next_y):
                                bfs.append((next_x, next_y))
                                visited.append((next_x, next_y))
            return ans

        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                ans = max(ans, countAreaofIsland(grid, x, y))
        return ans


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,0,0,0,0,0,0,0]]

solution = Solution()
print(solution.maxAreaOfIsland(grid))
