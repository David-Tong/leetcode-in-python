class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        def doCount(n):
            count = 9
            for x in range(n-1):
                count *= (9 - x)
            return count

        for x in range(1, n+1):
            dp[x] = doCount(x) + dp[x-1]
        return dp[n]


n = 3

solution = Solution()
print(solution.countNumbersWithUniqueDigits(n))
