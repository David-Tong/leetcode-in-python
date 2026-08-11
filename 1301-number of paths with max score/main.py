class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        # pre-process
        M = len(board)
        N = len(board[0])
        MODULO = 10 ** 9 + 7

        # process
        # dp init
        # scores[x][y] - the max score to reach board[x][y]
        # paths[x][y] - the number of paths to reach board[x][y]
        scores = [[float("-inf")] * N for _ in range(M)]
        paths = [[0] * N for _ in range(M)]
        scores[M - 1][N - 1] = 0
        paths[M - 1][N - 1] = 1

        # dp transfer
        # helper function
        def update(x, y, sx, sy):
            if board[x][y] == "E":
                board_score = 0
            else:
                board_score = int(board[x][y])
            if scores[sx][sy] + board_score > scores[x][y]:
                scores[x][y] = scores[sx][sy] + board_score
                paths[x][y] = paths[sx][sy]
            elif scores[sx][sy] + board_score == scores[x][y]:
                paths[x][y] = (paths[x][y] + paths[sx][sy]) % MODULO

        for x in range(M - 1, -1, -1):
            for y in range(N - 1, -1, -1):
                if x == 0 and y == 1:
                    pass
                if board[x][y] != "X":
                    # from down-right
                    if x + 1 < M and y + 1 < N:
                        update(x, y, x + 1, y + 1)
                    # from down
                    if x + 1 < M:
                        update(x, y, x + 1, y)
                    # from right
                    if y + 1 < N:
                        update(x, y, x, y + 1)
        # print(scores)
        # print(paths)

        if scores[0][0] == float("-inf"):
            return [0, 0]
        else:
            return [scores[0][0], paths[0][0]]


board = ["E23","2X2","12S"]
board = ["E12","1X1","21S"]
board = ["E11", "XXX", "11S"]

from random import randint
M = 3
N = 3
board = list()
for x in range(M):
    row = list()
    for y in range(N):
        if x == 0 and y == 0:
            row.append("E")
        elif x == M - 1 and y == N - 1:
            row.append("S")
        else:
            row.append(str(randint(1, 9)))
    board.append("".join(row))
print(board)

board = ["E61", "736", "13S"]

solution = Solution()
print(solution.pathsWithMaxScore(board))
