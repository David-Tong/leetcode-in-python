class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[x] - the max product of x integer break
        dp = [1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for x in range(3, n+1):
            dp[x] = max(dp[x-1], x-1,  dp[x-2] * 2, (x-2) * 2, dp[x-3] * 3, (x-3) * 3)
        return dp[n]


n = 2
n = 3
n = 10
#n = 58
n = 5
n = 4
n = 6

solution = Solution()
print(solution.integerBreak(n))
