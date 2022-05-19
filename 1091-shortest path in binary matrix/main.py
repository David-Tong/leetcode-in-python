class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        from collections import deque
        bfs = deque()
        if grid[0][0] == 0:
            bfs.append((0, 0))
        from collections import defaultdict
        visited = defaultdict(int)
        if grid[0][0] == 0:
            visited[(0, 0)] = 1

        while bfs:
            x, y = bfs.popleft()
            for direction in DIRECTIONS:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                    if grid[new_x][new_y] == 0:
                        dist = visited[(x, y)]
                        new_dist = dist + 1
                        if (new_x, new_y) not in visited or new_dist < visited[(new_x, new_y)]:
                            bfs.append((new_x, new_y))
                            visited[(new_x, new_y)] = new_dist

        if (N - 1, N - 1) in visited:
            return visited[(N - 1, N - 1)]
        else:
            return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[1,0,0],[1,1,0],[1,1,0]]
grid = [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,0,1],[0,1,1,1,1],[0,0,0,0,0]]
grid = [[0]]

solution = Solution()
print(solution.shortestPathBinaryMatrix(grid))
