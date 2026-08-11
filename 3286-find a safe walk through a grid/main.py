class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # process
        from collections import deque
        bfs = deque()
        bfs.append((0, 0, health if grid[0][0] == 0 else health - 1))
        visited = [[-1] * N for _ in range(M)]
        visited[0][0] = health if grid[0][0] == 0 else health - 1

        while bfs:
            x, y, h = bfs.popleft()
            if x == M - 1 and y == N - 1 and h >= 1:
                return True

            for dx, dy in DIRECTIONS:
                nx, ny, nh = x + dx, y + dy, h
                if 0 <= nx < M and 0 <= ny < N:
                    if grid[nx][ny] == 1:
                        nh -= 1
                        if nh <= 0:
                            continue
                    if visited[nx][ny] < nh:
                        visited[nx][ny] = nh
                        bfs.append((nx, ny, nh))
        return False


grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
health = 1

grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]
health = 3

grid = [[1,1,1],[1,0,1],[1,1,1]]
health = 5

grid = [[1,1,1,1]]
health = 5

"""
from random import randint
grid = [[randint(0, 1) for _ in range(50)] for _ in range(50)]
health = 25
print(grid)
"""

solution = Solution()
print(solution.findSafeWalk(grid, health))
