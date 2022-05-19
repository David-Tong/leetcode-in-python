class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        M = len(maze)
        N = len(maze[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        from collections import deque
        bfs = deque()
        bfs.append((entrance, 0))
        visited = [[0] * N for _ in range(M)]
        visited[entrance[0]][entrance[1]] = 1
        ans = float("inf")
        while bfs:
            size = len(bfs)
            for n in range(size):
                (x, y), steps = bfs.popleft()
                for direction in DIRECTIONS:
                    nx = x + direction[0]
                    ny = y + direction[1]
                    if 0 <= nx < M and 0 <= ny < N:
                        if maze[nx][ny] == ".":
                            if visited[nx][ny] == 0:
                                bfs.append(([nx, ny], steps + 1))
                                visited[nx][ny] = 1
                    else:
                        if [x, y] != entrance:
                            ans = min(ans, steps)
        return -1 if ans == float("inf") else ans


maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

#maze = [["+","+","+"],[".",".","."],["+","+","+"]]
#entrance = [1,0]

#maze = [[".","+"]]
#entrance = [0,0]

solution = Solution()
print(solution.nearestExit(maze, entrance))
