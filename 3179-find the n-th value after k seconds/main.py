class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # dp init
        dp = [[1] * n for _ in range(k + 1)]

        # dp transfer
        for x in range(1, k + 1):
            for y in range(1, n):
                dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % MODULO
        ans = dp[k][n - 1]
        return ans


n = 4
k = 5

n = 5
k = 3

solution = Solution()
print(solution.valueAfterKSeconds(n, k))
