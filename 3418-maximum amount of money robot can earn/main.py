class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(coins)
        N = len(coins[0])
        Z = 3

        # process
        # dp init
        # dp[x][y][z] - the maximum amount of coins robot can earn
        #               after reach coins[x][y] after z times neutralization
        dp = [[[float("-inf")] * 3 for _ in range(N)] for _ in range(M)]
        dp[0][0][0] = coins[0][0]
        # print(dp)

        # dp transfer
        # dp[x][y][z] = max(dp[x - 1][y][z], dp[x][y - 1][z])
        # dp[x][y][z] = max(dp[x][y][z - 1] + coins[x][y], dp[x][y][z]) if coins[x][y] < 0 and z < 2
        for x in range(M):
            for y in range(N):
                for z in range(Z):
                    if x > 0:
                        dp[x][y][z] = max(dp[x][y][z], dp[x - 1][y][z] + coins[x][y])
                    if y > 0:
                        dp[x][y][z] = max(dp[x][y][z], dp[x][y - 1][z] + coins[x][y])
                for z in range(Z - 1, 0, -1):
                    if coins[x][y] < 0:
                        dp[x][y][z] = max(dp[x][y][z - 1] - coins[x][y], dp[x][y][z])
        # print(dp)

        # post-process
        ans = max(dp[M - 1][N - 1])
        return ans


coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
coins = [[10,10,10],[10,10,10]]

"""
from random import randint
coins = [[randint(-10, 10) for _ in range(5)] for _ in range(5)]
print(coins)
"""
coins = [[-7, 1, -4, 9, -2], [-3, 4, -7, 2, 2], [3, -6, 0, -8, -6], [2, -9, 4, 6, -9], [2, -1, -2, 6, -9]]

solution = Solution()
print(solution.maximumAmount(coins))
