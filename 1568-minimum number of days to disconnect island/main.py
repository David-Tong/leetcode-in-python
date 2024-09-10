class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        total = 0
        for x in range(M):
            for y in range(N):
                total += grid[x][y]
        # conner case
        if total == 1:
            return 1

        def isConnected(start, expected):
            sx, sy = start
            from collections import deque
            bfs = deque()
            bfs.append((sx, sy))
            visit = [[False] * N for _ in range(M)]
            visit[sx][sy] = True

            count = 1
            while bfs:
                x, y = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if grid[nx][ny] == 1 and not visit[nx][ny]:
                            bfs.append((nx, ny))
                            visit[nx][ny] = True
                            count += 1
            return True if count == expected else False

        # find start
        start = None
        second = None
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1 and not start:
                    start = x, y
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if grid[nx][ny] == 1:
                                second = nx, ny
        if not second:
            return 0

        # process
        # the possible answer only can be 0, 1, or 2
        # when graph is not connected, return 0
        if not isConnected(start, total):
            return 0

        # search if we change one 1 cell to 0 cell will make it disconnected
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    if start != (x, y):
                        if not isConnected(start, total - 1):
                            return 1
                    else:
                        if not isConnected(second, total - 1):
                            return 1
                    grid[x][y] = 1

        # else
        return 2


grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
grid = [[1,1]]
grid = [[1,0,0,1],[1,0,0,1],[1,0,0,1]]
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0]]
grid = [[0,1,0],[1,1,1],[0,1,0]]
gird = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
grid = [[0,0,0],[0,1,0],[0,0,0]]

solution = Solution()
print(solution.minDays(grid))
