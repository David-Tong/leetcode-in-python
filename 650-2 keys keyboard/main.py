class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp init
        # dp[x] - min steps to reach x
        dp = [float("inf")] * (n + 1)
        dp[1] = 0

        # dp transfer
        for x in range(2, n + 1):
            for y in range(1, x // 2 + 1):
                if x % y == 0:
                    q = x // y
                    dp[x] = min(dp[x], dp[y] + 1 + (q - 1))

        return dp[n]


n = 3
n = 1
n = 10

solution = Solution()
print(solution.minSteps(n))
