class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 38
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for x in range(3, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2] + dp[x - 3]
        return dp[n]


n = 4
n = 1
n = 25

solution = Solution()
print(solution.tribonacci(n))
