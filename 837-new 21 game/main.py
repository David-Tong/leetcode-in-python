class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        # dp[x] - the probability to have n or fewer points
        dp = [0.0] * (k + maxPts)
        for x in range(maxPts):
            if k + x <= n:
                dp[k + x] = 1.0

        # calculate dp
        S = sum(dp[k:k + maxPts])
        for x in range(k - 1, -1, -1):
            dp[x] = S / maxPts
            S += dp[x] - dp[x + maxPts]
        return dp[0]


n = 10
k = 1
maxPts = 10

n = 6
k = 1
maxPts = 10

n = 21
k = 17
maxPts = 10

n = 28
k = 17
maxPts = 10

solution = Solution()
print(solution.new21Game(n, k, maxPts))
