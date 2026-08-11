class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # process
        visited = [[False for _ in range(N)] for _ in range(M)]

        # helper function
        from collections import deque
        def divisible(x, y):
            total = grid[x][y]
            bfs = deque()
            bfs.appendleft((x, y))
            visited[x][y] = True
            while bfs:
                x, y = bfs.pop()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if grid[nx][ny] > 0 and not visited[nx][ny]:
                            bfs.append((nx, ny))
                            visited[nx][ny] = True
                            total += grid[nx][ny]
            return total % k == 0

        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] > 0 and not visited[x][y]:
                    if divisible(x, y):
                        ans += 1
        return ans


grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
k = 5

grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]]
k = 3

"""
from random import randint
grid = [[randint(1, 100) for _ in range(100)] for _ in range(1000)]
k = 1
print(grid)
"""

grid = [[0,0,0],[0,0,1],[11,0,6],[0,10,2],[0,0,0],[8,0,0]]
k = 19

solution = Solution()
print(solution.countIslands(grid, k))
