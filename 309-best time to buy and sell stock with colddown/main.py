class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        hold = [[0] * 2 for x in range(N)]
        unhold = [[0] * 2 for x in range(N)]
        # hold[][0] don't sell at that day, hold[][1] sell at that day
        hold[0][0] = -1 * prices[0]
        hold[0][1] = float("-inf")
        unhold[0][0] = 0
        unhold[0][1] = float("-inf")

        for x in range(1, N):
            hold[x][0] = max(unhold[x-1][0] - prices[x], hold[x-1][0])
            hold[x][1] = float("-inf")
            unhold[x][0] = max(unhold[x-1][0], unhold[x-1][1])
            unhold[x][1] = max(hold[x-1][0] + prices[x], hold[x-1][1] + prices[x])
        return max(max(unhold))


prices = [1, 2, 3, 0, 2]
prices = [1]
prices = [5, 4, 3, 2, 1]
prices = [1, 2, 0, 10]
prices = [2, 1, 4]

solution = Solution()
print(solution.maxProfit(prices))
