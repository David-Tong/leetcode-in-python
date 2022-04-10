class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 31
        dp[0] = 0
        dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]


n = 2
n = 3
n = 4
n = 30
n = 1

solution = Solution()
print(solution.fib(n))
