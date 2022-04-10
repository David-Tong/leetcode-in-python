class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = [float("inf")] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for x in range(amount + 1):
            for coin in coins:
                if x - coin > 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]


coins = [1, 2, 5]
amount = 11

coins = [2]
amount = 3

coins = [1]
amount = 0

coins = [2]
amount = 1

solution = Solution()
print(solution.coinChange(coins, amount))
