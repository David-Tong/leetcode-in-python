class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        DIRECTIONS = ((-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2))

        board = [[0] * n for _ in range(n)]
        board[row][column] = 1

        for _ in range(k):
            n_board = [[0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if board[x][y] > 0:
                        for dx, dy in DIRECTIONS:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                n_board[nx][ny] += board[x][y] / 8.0
            board = n_board

        ans = 0
        for x in range(n):
            for y in range(n):
                ans += board[x][y]
        return ans


n = 3
k = 2
row = 0
column = 0

n = 1
k = 0
row = 0
column = 0

n = 25
k = 100
row = 5
column = 20

solution = Solution()
print(solution.knightProbability(n, k, row, column))
