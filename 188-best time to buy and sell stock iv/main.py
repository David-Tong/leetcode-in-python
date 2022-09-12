class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices) + 1

        # dp[x][y] - the max profit after y times trade (buy and sell) and x days
        K = 2 * k + 1
        dp = [[0] * K for _ in range(N)]

        # init
        dp[0][0] = 0
        for y in range(1, K):
            dp[0][y] = float("-inf")

        # dp transfer
        for x in range(1, N):
            # calculate max profit after y times trade and x days but without stock
            for y in range(0, K, 2):
                if x > 1 and y > 0:
                    dp[x][y] = max(dp[x - 1][y], dp[x - 1][y - 1] + prices[x - 1] - prices[x - 2])

            # calculate max profit after y times trade and x days but with stock
            for y in range(1, K, 2):
                if x > 1 and y > 0:
                    dp[x][y] = max(dp[x-1][y] + prices[x - 1] - prices[x - 2], dp[x-1][y-1])

        ans = float("-inf")
        for y in range(0, K, 2):
            ans = max(ans, dp[N - 1][y])
        return ans


k = 2
prices = [2,4,1]

k = 2
prices = [3,2,6,5,0,3]

solution = Solution()
print(solution.maxProfit(k, prices))
