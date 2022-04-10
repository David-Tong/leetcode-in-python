class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])

        def checkRow(board, row):
            columns = dict()
            for index in range(width):
                if board[row][index] != ".":
                    if board[row][index] in columns.keys():
                        return False
                    else:
                        columns[board[row][index]] = 1
            return True

        def checkColumn(board, column):
            rows = dict()
            for index in range(height):
                if board[index][column] != ".":
                    if board[index][column] in rows.keys():
                        return False
                    else:
                        rows[board[index][column]] = 1
            return True

        def checkSubSudoku(board, row, column):
            sudoku = dict()
            for i in range(3):
                for j in range(3):
                    if board[row+i][column+j] != ".":
                        if board[row+i][column+j] in sudoku.keys():
                            return False
                        else:
                            sudoku[board[row+i][column+j]] = 1
            return True

        for index in range(height):
            if not checkRow(board, index):
                return False

        for index in range(width):
            if not checkColumn(board, index):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not checkSubSudoku(board, i, j):
                    return False

        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]

solution = Solution()
print(solution.isValidSudoku(board))


