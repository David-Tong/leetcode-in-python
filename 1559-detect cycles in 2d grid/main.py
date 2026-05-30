class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        visited = [[False] * N for _ in range(M)]

        # helper function
        from collections import deque
        def cycle(x, y):
            bfs = deque()
            bfs.append((x, y, -1, -1))
            ch = grid[x][y]
            visited[x][y] = True
            while bfs:
                for _ in range(len(bfs)):
                    x, y, sx, sy = bfs.popleft()
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if grid[nx][ny] == ch:
                                if visited[nx][ny] == 0:
                                    bfs.append((nx, ny, x, y))
                                    visited[nx][ny] = True
                                else:
                                    if nx == sx and ny == sy:
                                        continue
                                    else:
                                        return True

            return False

        # process
        for x in range(M):
            for y in range(N):
                if visited[x][y] == 0:
                    if cycle(x, y):
                        return True
        return False


grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
grid = [["a","b","b"],["b","z","b"],["b","b","b"]]

"""
import string
import random
grid = [[random.choice(string.ascii_lowercase) for _ in range(300)] for _ in range(300)]
print(grid)
"""

solution = Solution()
print(solution.containsCycle(grid))

