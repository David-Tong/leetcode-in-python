class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def doValid(n, board, i, j):
            # check row
            count = 0
            for k in range(n):
                if board[i][k] == "Q":
                    count += 1
                if count > 1:
                    return False

            # check column
            count = 0
            for k in range(n):
                if board[k][j] == "Q":
                    count += 1
                if count > 1:
                    return False

            # check diagonal
            count = 0
            k = -1
            while i + k >= 0 and j + k >= 0:
                if board[i + k][j + k] == "Q":
                    count += 1
                k -= 1
            k = 1
            while i + k < n and j + k < n:
                if board[i + k][j + k] == "Q":
                    count += 1
                k += 1
            if count > 0:
                return False

            # check another diagonal
            count = 0
            k = -1
            while i + k >= 0 and j - k < n:
                if board[i + k][j - k] == "Q":
                    count += 1
                k -= 1
            k = 1
            while i + k < n and j - k >= 0:
                if board[i + k][j - k] == "Q":
                    count += 1
                k += 1
            if count > 0:
                return False

            return True

        def doSolve(n, board, row):
            if row >= n:
                self.ans += 1
                return

            for col in range(n):
                board[row][col] = "Q"
                if doValid(n, board, row, col):
                    doSolve(n, board, row + 1)
                board[row][col] = "."

        self.ans = 0
        board = [["."] * n for _ in range(n)]
        doSolve(n, board, 0)

        return self.ans


n = 4
n = 1
n = 9

solution = Solution()
print(solution.solveNQueens(n))
