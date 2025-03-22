from collections import deque


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[0] * N for _ in range(M)]

        # process
        # bfs helper
        def search(idx, sx, sy):
            from collections import deque
            bfs = deque()
            bfs.append((sx, sy))
            visited[sx][sy] = idx

            land = 0
            while bfs:
                x, y = bfs.popleft()
                land += 1
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if grid[nx][ny] == 1:
                            if visited[nx][ny] == 0:
                                bfs.append((nx, ny))
                                visited[nx][ny] = idx
            return land

        from collections import defaultdict
        lands = defaultdict(int)

        idx = 1
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1 and visited[x][y] == 0:
                    land = search(idx, x, y)
                    lands[idx] = land
                    idx += 1
        # print(lands)

        # post-process
        ans = 0
        has_water = False
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0:
                    has_water = True
                    connected = set()
                    large_land = 1
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if grid[nx][ny] == 1:
                                connected.add(visited[nx][ny])
                    for idx in connected:
                        large_land += lands[idx]
                    ans = max(ans, large_land)
        return ans if has_water else M * N


grid = [[1,0],[0,1]]
grid = [[1,1],[1,0]]
grid = [[1,1],[1,1]]

solution = Solution()
print(solution.largestIsland(grid))
