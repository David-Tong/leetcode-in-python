class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # pre-process
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        M = len(grid)
        N = len(grid[0])

        # shortcut
        if M == 1 and N == 1:
            return True

        def connect(cell, cell2, direction):
            type, type2 = grid[cell[0]][cell[1]], grid[cell2[0]][cell2[1]]
            if type == 1:
                if type2 == 1 or type2 == 3 or type2 == 5:
                    if direction == (0, 1):
                        return True
                if type2 == 1 or type2 == 4 or type2 == 6:
                    if direction == (0, -1):
                        return True
            elif type == 2:
                if type2 == 2 or type2 == 5 or type2 == 6:
                    if direction == (1, 0):
                        return True
                if type2 == 2 or type2 == 3 or type2 == 4:
                    if direction == (-1, 0):
                        return True
            elif type == 3:
                if type2 == 2 or type2 == 5 or type2 == 6:
                    if direction == (1, 0):
                        return True
                if type2 == 1 or type2 == 4 or type2 == 6:
                    if direction == (0, -1):
                        return True
            elif type == 4:
                if type2 == 1 or type2 == 3 or type2 == 5:
                    if direction == (0, 1):
                        return True
                if type2 == 2 or type2 == 5 or type2 == 6:
                    if direction == (1, 0):
                        return True
            elif type == 5:
                if type2 == 1 or type2 == 4 or type2 == 6:
                    if direction == (0, -1):
                        return True
                if type2 == 2 or type2 == 3 or type2 == 4:
                    if direction == (-1, 0):
                        return True
            elif type == 6:
                if type2 == 1 or type2 == 3 or type2 == 5:
                    if direction == (0, 1):
                        return True
                if type2 == 2 or type2 == 3 or type2 == 4:
                    if direction == (-1, 0):
                        return True

        # process
        # bfs
        from collections import deque
        bfs = deque()
        bfs.append((0, 0))
        visited = [[False] * N for _ in range(M)]
        visited[0][0] = True
        while bfs:
            cell = bfs.popleft()
            for direction in DIRECTIONS:
                cell2 = (cell[0] + direction[0], cell[1] + direction[1])
                if 0 <= cell2[0] < M and 0 <= cell2[1] < N:
                    if not visited[cell2[0]][cell2[1]]:
                        if connect(cell, cell2, direction):
                            if cell2[0] == M - 1 and cell2[1] == N - 1:
                                return True
                            bfs.append(cell2)
                            visited[cell2[0]][cell2[1]] = True
        return False


grid = [[2,4,3],[6,5,2]]
grid = [[1,2,1],[1,2,1]]
grid = [[1,1,2]]
grid = [[1]]
grid = [[3,4,3,4,3,4,3],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[6,5,6,5,6,5,6]]

"""
from random import randint
M, N = 300, 300
grid = [[0] * N for _ in range(M)]
for x in range(M):
    for y in range(N):
        grid[x][y] = randint(1, 6)
print(grid)
"""

solution = Solution()
print(solution.hasValidPath(grid))
