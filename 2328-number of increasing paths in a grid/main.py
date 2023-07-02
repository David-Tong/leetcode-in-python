class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        MODULO = 10 ** 9 + 7
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        import sys
        sys.setrecursionlimit(M * N + 10)

        # cache
        from collections import defaultdict
        self.cache = defaultdict(int)

        def doPaths(x, y):
            key = str(x) + "-" + str(y)
            if key in self.cache:
                return self.cache[key]

            paths = 1
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if grid[x][y] < grid[nx][ny]:
                        paths += doPaths(nx, ny)

            paths %= MODULO

            self.cache[key] = paths
            return paths

        ans = 0
        for x in range(M):
            for y in range(N):
                ans += doPaths(x, y)
        #print(self.cache)
        return ans % MODULO


grid = [[1,1],[3,4]]
grid = [[1],[2]]
grid = [[1,2],[4,3]]
grid = [[1,2],[4,3],[5,6],[7,8]]

M = 100
N = 100
grid = [[1] * N for _ in range(M)]
print(grid)

for x in range(M):
    for y in range(N):
        grid[x][y] = x * M + y + 1
print(grid)

solution = Solution()
print(solution.countPaths(grid))
