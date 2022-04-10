class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for x in range(2)]

        old = 0
        now = 0
        for y in range(N):
            dp[now][y] = matrix[now][y]

        for x in range(1, M):
            old = now
            now = 1 - now
            for y in range(N):
                if y == 0:
                    dp[now][y] = min(dp[old][y], dp[old][y+1])
                elif y == N - 1:
                    dp[now][y] = min(dp[old][y-1], dp[old][y])
                else:
                    dp[now][y] = min(dp[old][y-1], dp[old][y], dp[old][y+1])
                dp[now][y] += matrix[x][y]

        return min(dp[now])


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
#matrix = [[-19, 57], [-40, -5]]

solution = Solution()
print(solution.minFallingPathSum(matrix))
