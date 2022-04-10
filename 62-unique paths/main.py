class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for x in range(m)]
        dp[0][0] = 1
        for x in range(m):
            for y in range(n):
                if x > 0:
                    dp[x][y] += dp[x-1][y]
                if y > 0:
                    dp[x][y] += dp[x][y-1]
        return dp[m-1][n-1]


m = 3
n = 7

m = 3
n = 2

m = 1
n = 1

solution = Solution()
print(solution.uniquePaths(m, n))
