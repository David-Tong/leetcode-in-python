class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # pre-process
        M = len(board)
        N = len(board[0])

        rows = [[False] * 10 for _ in range(M)]
        cols = [[False] * 10 for _ in range(N)]
        subboxes = [[[False] * 10 for _ in range(N // 3)] for _ in range(M // 3)]

        for x in range(M):
            for y in range(N):
                if board[x][y] != '.':
                    num = int(board[x][y])
                    rows[x][num] = True
                    cols[y][num] = True
                    subboxes[x // 3][y // 3][num] = True

        """
        print(rows)
        print(cols)
        print(subboxes)
        """

        # helper function
        def isValid(x, y, num):
            if rows[x][num]:
                return False
            if cols[y][num]:
                return False
            if subboxes[x // 3][y // 3][num]:
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
                    if isValid(x, y, num):
                        rows[x][num] = True
                        cols[y][num] = True
                        subboxes[x // 3][y // 3][num] = True
                        board[x][y] = str(num)
                        if dfs(x, y + 1):
                            return True
                        board[x][y] = '.'
                        rows[x][num] = False
                        cols[y][num] = False
                        subboxes[x // 3][y // 3][num] = False
            else:
                if dfs(x, y + 1):
                    return True
            return False

        dfs(0, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "9", ".", ".", "1", ".", ".", "3", "."],
         [".", ".", "6", ".", "2", ".", "7", ".", "."],
         [".", ".", ".", "3", ".", "4", ".", ".", "."],
         ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "2", "5", ".", "6", "4", ".", "."],
         [".", "8", ".", ".", ".", ".", ".", "1", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

solution = Solution()
solution.solveSudoku(board)
print(board)
