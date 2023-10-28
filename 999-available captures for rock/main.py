class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        M = len(board)
        N = len(board[0])

        # get rook
        rx, ry = -1, -1
        for x in range(M):
            for y in range(N):
                if board[x][y] == 'R':
                    rx, ry = x, y
                    break

        # search cardinal directions
        ans = 0
        # north
        for x in range(rx - 1, -1, -1):
            if board[x][ry] == "B":
                break
            elif board[x][ry] == "p":
                ans += 1
                break
        # south
        for x in range(rx + 1, M, 1):
            if board[x][ry] == "B":
                break
            elif board[x][ry] == "p":
                ans += 1
                break
        # east
        for y in range(ry + 1, N, 1):
            if board[rx][y] == "B":
                break
            elif board[rx][y] == "p":
                ans += 1
                break
        # west
        for y in range(ry - 1, -1, -1):
            if board[rx][y] == "B":
                break
            elif board[rx][y] == "p":
                ans += 1
                break
        return ans


board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

solution = Solution()
print(solution.numRookCaptures(board))
