class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        self.pathes = list()
        visited = [[0] * N for _ in range(M)]
        to_visit = 0

        sx = 0
        sy = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0:
                    to_visit += 1
                elif grid[x][y] == 1:
                    sx = x
                    sy = y

        def doPath(x, y, path, count, visited, grid):
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if grid[nx][ny] == 0:
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            doPath(nx, ny, path + [(nx, ny)], count + 1, visited, grid)
                            visited[nx][ny] = 0
                    elif grid[nx][ny] == 2:
                        if to_visit == count:
                            path.append((nx, ny))
                            self.pathes.append(path)

        doPath(sx, sy, [(sx, sy)], 0, visited, grid)
        return len(self.pathes)


grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
grid = [[0,1],[2,0]]

solution = Solution()
print(solution.uniquePathsIII(grid))
