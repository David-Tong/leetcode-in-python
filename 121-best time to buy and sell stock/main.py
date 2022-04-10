class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        hold = [0] * N
        unhold = [0] * N
        hold[0] = -1 * prices[0]
        unhold[0] = 0
        for x in range(1, N):
            hold[x] = max(hold[x-1], -1 * prices[x])
            unhold[x] = max(unhold[x-1], hold[x-1] + prices[x])
        return max(unhold)


prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
prices = [5]

solution = Solution()
print(solution.maxProfit(prices))
