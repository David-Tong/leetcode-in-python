class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        from math import sqrt
        M = len(matrix)
        N = len(matrix[0])
        row_prefix = [[0] * N for _ in range(M)]
        col_prefix = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if matrix[x][y] == "1":
                    if y > 0:
                        row_prefix[x][y] = row_prefix[x][y-1] + 1
                    else:
                        row_prefix[x][y] = 1

        for y in range(N):
            for x in range(M):
                if matrix[x][y] == "1":
                    if x > 0:
                        col_prefix[x][y] = col_prefix[x-1][y] + 1
                    else:
                        col_prefix[x][y] = 1

        dp = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                if matrix[x][y] == "1":
                    dp[x][y] = 1
                if x > 0 and y > 0:
                    if dp[x-1][y-1] > 0:
                        root = int(sqrt(dp[x-1][y-1]))
                        for z in range(root, -1, -1):
                            if row_prefix[x][y] > z and col_prefix[x][y] > z:
                                dp[x][y] = (z + 1) ** 2
                                break

        ans = 0
        for x in range(M):
            for y in range(N):
                ans = max(ans, dp[x][y])
        return ans


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
matrix = [["0"]]
matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]

solution = Solution()
print(solution.maximalSquare(matrix))
