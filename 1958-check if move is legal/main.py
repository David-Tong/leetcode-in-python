class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        # pre-process
        M = len(board)
        N = len(board[0])

        def check(sx, sy, dx, dy, color):
            opposite_color = 'B' if color == 'W' else 'W'
            opposites = 0
            x, y = sx + dx, sy + dy
            while 0 <= x < M and 0 <= y < N:
                if board[x][y] == opposite_color:
                    opposites += 1
                elif board[x][y] == color:
                    if opposites > 0:
                        return True
                    else:
                        return False
                else:
                    return False
                x, y = x + dx, y + dy
            return False

        # process
        DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        for dx, dy in DIRECTION:
            if check(rMove, cMove, dx, dy, color):
                return True
        return False


board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
rMove = 4
cMove = 3
color = "B"

board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]
rMove = 4
cMove = 4
color = "W"

solution = Solution()
print(solution.checkMove(board, rMove, cMove, color))
