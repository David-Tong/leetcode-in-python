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
        dp = [[0] * (target + 1) for _ in range(2)]
        old = 0
        new = 0
        dp[old][0] = 1

        for x in range(n):
            old = new
            new = 1 - old
            for z in range(target + 1):
                dp[new][z] = 0
            for y in range(k):
                for z in range(target):
                    if z - y >= 0:
                        dp[new][z + 1] += dp[old][z - y]
        return dp[new][target] % MODULO


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
