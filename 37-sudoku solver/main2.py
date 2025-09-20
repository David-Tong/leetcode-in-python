class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # pre-process
        M = len(board)
        N = len(board[0])

        # helper function
        # is valid
        def isValid(x, y, num):
            # check the row
            for col in range(N):
                if board[x][col] == num:
                    return False

            # check the col
            for row in range(M):
                if board[row][y] == num:
                    return False

            # check the sub-boxes
            for row in range(M // 3):
                for col in range(N // 3):
                    if board[(x // 3) * 3 + row][(y // 3) * 3 + col] == num:
                        return False
                    
            return True

        # process
        def dfs(x, y):
            if x == M - 1 and y == N:
                return True

            if y == M:
                x += 1
                y = 0

            # place a number
            if board[x][y] == ".":
                for num in range(1, 10):
                    num = str(num)
                    if isValid(x, y, num):
                        board[x][y] = num
                        if dfs(x, y + 1):
                            return True
                        board[x][y] = '.'
            else:
                if dfs(x, y + 1):
                    return True
            return  False

        dfs(0, 0)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

board = [[".",".",".",".",".",".",".",".","."],
         [".","9",".",".","1",".",".","3","."],
         [".",".","6",".","2",".","7",".","."],
         [".",".",".","3",".","4",".",".","."],
         ["2","1",".",".",".",".",".","9","8"],
         [".",".",".",".",".",".",".",".","."],
         [".",".","2","5",".","6","4",".","."],
         [".","8",".",".",".",".",".","1","."],
         [".",".",".",".",".",".",".",".","."]]

solution = Solution()
solution.solveSudoku(board)
print(board)
