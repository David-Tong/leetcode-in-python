class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULE = 10 ** 9 + 7
        N = 1001
        dp = [2] * N
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for x in range(n + 1):
            for y in range(1, n):
                if x - y >= 0:
                    if y == 1 or y == 2:
                        dp[x] += dp[x - y]
                    else:
                        dp[x] += 2 * dp[x - y]
        return dp[n] % MODULE


n = 4

solution = Solution()
print(solution.numTilings(n))
