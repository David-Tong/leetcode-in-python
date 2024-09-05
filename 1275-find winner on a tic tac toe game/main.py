class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        N = 3

        board = [[''] * 3 for _ in range(N)]
        cross = True
        for move in moves:
            x, y = move
            if cross:
                board[x][y] = 'x'
            else:
                board[x][y] = 'o'
            cross = not cross

        # check rows
        for x in range(N):
            check = True
            for y in range(N):
                if board[x][y] != board[x][0]:
                    check = False
                    break
            if check:
                if board[x][0] == 'x':
                    return 'A'
                elif board[x][0] == 'o':
                    return 'B'

        # check columns
        for y in range(N):
            for x in range(N):
                check = True
                if board[x][y] != board[0][y]:
                    check = False
                    break
            if check:
                if board[0][y] == 'x':
                    return 'A'
                elif board[0][y] == 'o':
                    return 'B'

        # check diagonals
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'x':
                return 'A'
            elif board[0][0] == 'o':
                return 'B'

        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'x':
                return 'A'
            elif board[0][2] == 'o':
                return 'B'

        if len(moves) < N * N:
            return "Pending"
        else:
            return "Draw"


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves = [[0,0],[1,1]]

solution = Solution()
print(solution.tictactoe(moves))
