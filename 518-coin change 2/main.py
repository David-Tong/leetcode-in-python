class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        N = amount + 1
        dp = [0] * N
        dp[0] = 1
        for coin in coins:
            for x in range(coin, N):
                dp[x] += dp[x - coin]
        return dp[N - 1]


amount = 5
coins = [1, 2, 5]

amount = 3
coins = [2]

amount = 10
coins = [10]

solution = Solution()
print(solution.change(amount, coins))
