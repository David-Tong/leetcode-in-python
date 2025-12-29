class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        # dp init
        L = len(prices)
        buy = [[float('-inf')] * (k + 1) for _ in range(L + 1)]
        sell = [[float('-inf')] * (k + 1) for _ in range(L + 1)]
        short_sell = [[float('-inf')] * (k + 1) for _ in range(L + 1)]
        short_buy = [[float('-inf')] * (k + 1) for _ in range(L + 1)]
        for x in range(L + 1):
            sell[x][0] = 0
            short_buy[x][0] = 0

        # dp transfer
        for x in range(L):
            for y in range(k):
                buy[x + 1][y + 1] = max(buy[x][y + 1], max(sell[x][y] - prices[x], short_buy[x][y] - prices[x]))
                sell[x + 1][y + 1] = max(sell[x][y + 1], buy[x][y + 1] + prices[x])
                short_sell[x + 1][y + 1] = max(short_sell[x][y + 1], max(sell[x][y] + prices[x], short_buy[x][y] + prices[x]))
                short_buy[x + 1][y + 1] = max(short_buy[x][y + 1], short_sell[x][y + 1] - prices[x])

        """
        print(buy)
        print(sell)
        print(short_sell)
        print(short_buy)
        """

        ans = float("-inf")
        for y in range(k + 1):
            ans = max(ans, sell[L][y])
            ans = max(ans, short_buy[L][y])
        return ans


prices = [1,7,9,8,2]
k = 2

prices = [12,16,19,19,8,1,19,13,9]
k = 3

"""
from random import randint
n = 10
prices = [randint(1, 10 ** 3) for _ in range(n)]
k = 5
print(prices)
"""

prices = [14,6,10,19]
k = 1

solution = Solution()
print(solution.maximumProfit(prices, k))
