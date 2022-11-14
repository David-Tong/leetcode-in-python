class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # dp[x] - the number of way of dice rolls to get target sum of x
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for x in range(n):
            for y in range(k):
                for z in range(target):
                    if z - y >= 0:
                        dp[x + 1][z + 1] += dp[x][z - y]
        return dp[n][target] % MODULO


n = 1
k = 6
target = 3

n = 2
k = 6
target = 7

n = 30
k = 30
target = 500

n = 30
k = 30
target = 1000

solution = Solution()
print(solution.numRollsToTarget(n, k, target))
