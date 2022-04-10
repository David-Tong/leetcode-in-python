class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = n + 1
        dp = [0] * N
        dp[0] = 1
        dp[1] = 1
        for x in range(2, N):
            for y in range(x):
                dp[x] += dp[y] * dp[x-y-1]
        return dp[n]


n = 4

solution = Solution()
print(solution.numTrees(n))
