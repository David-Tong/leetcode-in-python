class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        import string

        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # pre-process
        K = 0
        start = None
        for x in range(M):
            for y in range(N):
                if grid[x][y] in string.ascii_lowercase:
                    K += 1
                if grid[x][y] == '@':
                    start = (x, y)

        from collections import deque
        bfs = deque()
        from collections import defaultdict
        visited = [[None] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                visited[x][y] = defaultdict(bool)

        # start bfs
        keys = set()
        bfs.append((start[0], start[1], keys))
        visited[start[0]][start[1]][""] = True

        import copy
        steps = 0
        while bfs:
            steps += 1
            size = len(bfs)
            for _ in range(size):
                x, y, old_keys = bfs.popleft()
                for dx, dy in DIRECTIONS:
                    keys = copy.deepcopy(old_keys)
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        # block by wall
                        if grid[nx][ny] == "#":
                            continue
                        # block by lock
                        if grid[nx][ny] in string.ascii_uppercase:
                            if string.lower(grid[nx][ny]) not in keys:
                                continue
                        # visited
                        key = "-".join(sorted(keys))
                        if key in visited[nx][ny] and visited[nx][ny][key]:
                            continue
                        # add key
                        if grid[nx][ny] in string.ascii_lowercase:
                            keys.add(grid[nx][ny])

                        # end condition
                        if len(keys) == K:
                            return steps

                        # keep search
                        key = "-".join(sorted(keys))
                        visited[nx][ny][key] = True
                        bfs.append((nx, ny, keys))
        return -1


grid = ["@.a..","###.#","b.A.B"]
grid = ["@..aA","..B#.","....b"]
grid = ["@Aa"]
grid = ["@...a",".###A","b.BCc"]
grid = [".#.b.","A.#aB","#d...","@.cC.","D...#"]

solution = Solution()
print(solution.shortestPathAllKeys(grid))