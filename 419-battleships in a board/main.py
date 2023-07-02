class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        M = len(board)
        N = len(board[0])

        def removeHorizontally(x, y):
            if y > 0 and board[x][y - 1] == 'X':
                ny = y - 1
                while ny >= 0 and board[x][ny] == 'X':
                    board[x][ny] = '.'
                    ny -= 1
            if y < N - 1 and board[x][y + 1] == 'X':
                ny = y + 1
                while ny < N and board[x][ny] == 'X':
                    board[x][ny] = '.'
                    ny += 1
            board[x][y] = '.'

        def removeVertically(x, y):
            if x > 0 and board[x - 1][y] == 'X':
                nx = x - 1
                while nx >= 0 and board[nx][y] == 'X':
                    board[nx][y] = '.'
                    nx -= 1
            if x < M - 1 and board[x + 1][y] == 'X':
                nx = x + 1
                while nx < M and board[nx][y] == 'X':
                    board[nx][y] = '.'
                    nx += 1
            board[x][y] = '.'

        # search
        ans = 0
        for x in range(M):
            for y in range(N):
                if board[x][y] == 'X':
                    removeVertically(x, y)
                    removeHorizontally(x, y)
                    ans += 1

        return ans


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board = [["."]]
board = [["X",".","X","."],[".",".","X","."],[".",".",".","."],[".",".","X","."]]
board = [["X",".","X","."],[".",".",".","X"],[".",".","X","."],[".",".",".","X"]]

solution = Solution()
print(solution.countBattleships(board))
