class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        for x in range(1, n + 1):
            if x - 1 >= 0:
                dp[x] += dp[x-1]
            if x - 2 >= 0:
                dp[x] += dp[x-2]
        return dp[n]


n = 2
n = 3
n = 45

solution = Solution()
print(solution.climbStairs(n))
