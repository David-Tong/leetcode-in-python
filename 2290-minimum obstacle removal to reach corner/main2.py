class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # bfs
        def canReach(removals):
            from collections import deque
            bfs = deque()
            bfs.append((0, 0, removals))
            visited = [[float("-inf")] * N for _ in range(M)]
            visited[0][0] = removals

            while bfs:
                size = len(bfs)
                for _ in range(size):
                    x, y, removals = bfs.popleft()
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if nx == M - 1 and ny == N - 1:
                                return True
                            if visited[nx][ny] < removals:
                                visited[nx][ny] = removals
                                if grid[nx][ny] == 1:
                                    if removals > 0:
                                        bfs.append((nx, ny, removals - 1))
                                else:
                                    bfs.append((nx, ny, removals))
            return False

        # process
        # binary search
        left, right = 0, M + N
        while left + 1 < right:
            middle = (left + right) // 2
            print(middle)
            if canReach(middle):
                right = middle
            else:
                left = middle + 1

        if canReach(left):
            return left
        else:
            return right


grid = [[0,1,1],[1,1,0],[1,1,0]]
grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]

import random
def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        matrix.append(row)
    matrix[0][0] = 0
    matrix[rows - 1][cols - 1] = 0
    return matrix

grid = generate_random_matrix(50, 50)
print(grid)

solution = Solution()
print(solution.minimumObstacles(grid))
