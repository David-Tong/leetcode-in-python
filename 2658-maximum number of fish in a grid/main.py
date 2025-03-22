class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * N for _ in range(M)]

        # process
        # helper function
        def findFish(sx, sy):
            from collections import deque
            bfs = deque()
            bfs.append((sx, sy))
            visited[sx][sy] = True

            ans = 0
            while bfs:
                x, y = bfs.popleft()
                ans += grid[x][y]
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if grid[nx][ny] != 0 and not visited[nx][ny]:
                            bfs.append((nx, ny))
                            visited[nx][ny] = True
            return ans

        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] != 0 and not visited[x][y]:
                    ans = max(ans, findFish(x, y))
        return ans


grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
grid = [[0]]

solution = Solution()
print(solution.findMaxFish(grid))
