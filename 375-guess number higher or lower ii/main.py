class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = n + 1
        # dp[x][y] - the minimum amount of money to win in range [x, y]
        dp = [[0] * N for _ in range(N)]

        for y in range(N):
            for x in range(1, N):
                if y == 0:
                    continue
                else:
                    if x + y < N:
                        mini = float("inf")
                        for z in range(y + 1):
                            maxi = 0
                            if z > 0 and x + z - 1 < N:
                                maxi = max(maxi, dp[x][x + z - 1] + x + z)
                            if z < y and x + z + 1 < N:
                                maxi = max(maxi, x + z + dp[x + z + 1][x + y])
                            mini = min(mini, maxi)
                        dp[x][x+y] = mini
        return dp[1][n]


n = 2
n = 3
n = 10
n = 50
n = 100
n = 200

solution = Solution()
print(solution.getMoneyAmount(n))
