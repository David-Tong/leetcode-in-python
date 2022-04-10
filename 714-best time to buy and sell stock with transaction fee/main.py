class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        N = len(prices)
        hold = [0] * N
        unhold = [0] * N
        hold[0] = -1 * prices[0]
        unhold[0] = 0

        for x in range(1, N):
            hold[x] = max(unhold[x-1] - prices[x], hold[x-1])
            unhold[x] = max(hold[x-1] + prices[x] - fee, unhold[x-1])
        return max(unhold)


prices = [1, 3, 2, 8, 4, 9]
fee = 2

prices = [1, 3, 7, 5, 10, 3]
fee = 3

prices = [1]
fee = 1

prices = [1, 4, 2, 3]
fee = 2

solution = Solution()
print(solution.maxProfit(prices, fee))
