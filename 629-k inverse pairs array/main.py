class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # dp[x][y] - the number of array with y inverse pairs of numbers from 1 to x
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = (dp[i][j - 1] if j - 1 >= 0 else 0) - (dp[i - 1][j - i] if j - i >= 0 else 0) + dp[i - 1][j]
                dp[i][j] %= MOD

        return dp[n][k]


n = 3
k = 0

n = 3
k = 1

n = 3
k = 2

n = 3
k = 3

solution = Solution()
print(solution.kInversePairs(n, k))
