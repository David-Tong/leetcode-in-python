class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        oes = []

        from collections import deque
        bfs = deque()
        visited = set()
        for x in [0, M - 1]:
            for y in range(N):
                if board[x][y] == "O":
                    if (x, y) not in visited:
                        bfs.append((x, y))
                        visited.add((x, y))

        for y in [0, N - 1]:
            for x in range(M):
                if board[x][y] == "O":
                    if (x, y) not in visited:
                        bfs.append((x, y))
                        visited.add((x, y))

        while bfs:
            point = bfs.popleft()
            for direction in DIRECTIONS:
                x = point[0] + direction[0]
                y = point[1] + direction[1]
                if x >= 0 and x < M and y >= 0 and y < N:
                    if board[x][y] == "O":
                        if (x, y) not in visited:
                            bfs.append((x, y))
                            visited.add((x, y))

        for x in range(M):
            for y in range(N):
                if board[x][y] == "O":
                    if (x, y) not in visited:
                        board[x][y] = "X"


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#board = [["X"]]
#board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]

solution = Solution()
solution.solve(board)
print(board)
