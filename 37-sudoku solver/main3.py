class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])

        def isValid(board, x, y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(M):
                if board[i][y] == tmp:
                    return False
            for j in range(N):
                if board[x][j] == tmp:
                    return False
            for i in range(M // 3):
                for j in range(N // 3):
                    if board[int(x / 3) * 3 + i][int(y / 3) * 3 + j] == tmp:
                        return False
            board[x][y] = tmp
            return True

        def doSolve(board, nums, i, j):
            if i == M - 1 and j == N:
                return True

            if j == M:
                i += 1
                j = 0

            if j == 0:
                nums = [str(_) for _ in range(1, 10)]
                for num in board[i]:
                    if num != ".":
                        nums.remove(num)

            if board[i][j] == ".":
                for k in range(len(nums)):
                    board[i][j] = nums[k]
                    if isValid(board, i, j):
                        if doSolve(board, nums[:k] + nums[k + 1:], i, j + 1):
                            return True
                    board[i][j] = "."
            else:
                if doSolve(board, nums, i, j + 1):
                    return True
            return False

        doSolve(board, [], 0, 0)


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
