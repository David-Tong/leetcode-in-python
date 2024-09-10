class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULE = 10 ** 9 + 7

        # dp[x][0] - the number of ways to tile a 2 * x board
        # dp[x][1] - the number of ways to tile a 2 * x board with the most right bottom tile missing
        # dp[x][2] - the number of ways to tile a 2 * x board with the most right up tile missing
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for x in range(2, n + 1):
            dp[x][0] = dp[x - 1][0] + dp[x - 2][0] + dp[x - 1][1] + dp[x - 1][2]
            dp[x][1] = dp[x - 2][0] + dp[x - 1][2]
            dp[x][2] = dp[x - 2][0] + dp[x - 1][1]
        return dp[n][0] % MODULE


n = 4

solution = Solution()
print(solution.numTilings(n))
