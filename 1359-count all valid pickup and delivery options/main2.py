class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10e8 + 7
        dp = [0] * n
        dp[0] = 1
        for x in range(1, n):
            dp[x] = dp[x - 1] * (2 * x + 1) + dp[x - 1] * (2 * x + 1) * 2 * x // 2
            dp[x] = dp[x] % MODULO

        return int(dp[n-1])


n = 2
n = 3
n = 500

solution = Solution()
print(solution.countOrders(n))
