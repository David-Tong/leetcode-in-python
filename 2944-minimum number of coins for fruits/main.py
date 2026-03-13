class Solution(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # pre-process
        L = len(prices)

        # process
        # dp init
        # dp[x][0] - the minimum number of coins to get all fruits[:x + 1] without purchasing xth fruit
        # dp[x][1] - the minimum number of coins to get all fruits[:x + 1] with purchasing xth fruit
        dp = [[float("inf")] * 2 for _ in range(L)]
        dp[0][1] = prices[0]

        # dp transfer
        # dp[x][0] - min(dp[y][1]) for y in [y, y + y + 1] when 2y + 1 = x
        # dp[x][1] - min(dp[x - 1][0], dp[x][0]) + prices[x]
        for x in range(1, L):
            # update dp[x][0]
            y = x - 1
            while y + y + 1 >= x:
                dp[x][0] = min(dp[x][0], dp[y][1])
                y -= 1
            # update dp[x][1]
            dp[x][1] = min(dp[x - 1][0], dp[x][0]) + prices[x]
        # print(dp)

        # post-process
        ans = min(dp[L - 1])
        return ans


prices = [3,1,2]
prices = [1,10,1,1]
prices = [26,18,6,12,49,7,45,45]

from random import randint
prices = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
print(prices)

solution = Solution()
print(solution.minimumCoins(prices))
