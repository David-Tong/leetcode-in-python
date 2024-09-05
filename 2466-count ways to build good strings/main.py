class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # dp[x] = the number of different good strings with length of x
        dp = [0] * (high + 1)
        dp[0] = 1
        for x in range(1, high + 1):
            if x - zero >= 0:
                dp[x] += dp[x - zero]
            if x - one >= 0:
                dp[x] += dp[x - one]

        ans = 0
        for x in range(low, high + 1):
            ans += dp[x]

        return ans % MODULO


low = 3
high = 3
zero = 1
one = 1

low = 2
high = 3
zero = 1
one = 2

low = 1
high = 1
zero = 1
one = 1

solution = Solution()
print(solution.countGoodStrings(low, high, zero, one))
