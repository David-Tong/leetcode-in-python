class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        hold = [[0] * 3 for x in range(N)]
        unhold = [[0] * 3 for x in range(N)]
        hold[0][0] = -1 * prices[0]
        hold[0][1] = float("-inf")
        hold[0][2] = float("-inf")
        unhold[0][0] = 0
        unhold[0][1] = float("-inf")
        unhold[0][2] = float("-inf")
        ans = 0
        for x in range(1, N):
            unhold[x][0] = 0
            unhold[x][1] = max(hold[x-1][0] + prices[x], unhold[x-1][1])
            unhold[x][2] = max(hold[x-1][1] + prices[x], unhold[x-1][2])
            hold[x][0] = max(-1 * prices[x], hold[x-1][0])
            hold[x][1] = max(unhold[x-1][1] - prices[x], hold[x-1][1])
            hold[x][2] = float("-inf")
            ans = max(ans, max(unhold[x][1], unhold[x][2]))
        return ans


prices = [3, 3, 5, 0, 0, 3, 1, 4]
#prices = [1, 2, 3, 4, 5]
#prices = [7, 6, 4, 3, 1]

solution = Solution()
print(solution.maxProfit(prices))
