class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        def checkNeighbors(board, x, y):
            live = dead = 0
            for direction in DIRECTIONS:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                    if board[new_x][new_y][0] == "1":
                        live += 1
                    else:
                        dead += 1
            return live, dead

        def checkRules(board, x, y):
            live, dead = checkNeighbors(board, x, y)
            if board[x][y][0] == "1":
                # rule 1
                if live < 2:
                    board[x][y] += "0"
                # rule 3
                elif live > 3:
                    board[x][y] += "0"
                # rule 2
                else:
                    board[x][y] += "1"
            else:
                # rule 4
                if live == 3:
                    board[x][y] += "1"
                else:
                    board[x][y] += "0"

        # convert to string, for in-place algorithm
        for x in range(M):
            for y in range(N):
                board[x][y] = str(board[x][y])

        # run game of life
        for x in range(M):
            for y in range(N):
                checkRules(board, x, y)

        # process board, to return
        for x in range(M):
            for y in range(N):
                board[x][y] = int(board[x][y][1])


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]

solution = Solution()
solution.gameOfLife(board)
print(board)
