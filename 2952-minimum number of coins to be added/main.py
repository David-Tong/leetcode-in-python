class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        # pre-process
        L = len(coins)
        coins = sorted(coins)
        coins.append(target)

        # process
        idx = 0
        total = 0
        ans = 0
        if 1 not in coins:
            coins = [1] + coins
            ans = 1
            L += 1
        while idx < L:
            total += coins[idx]
            while total + 1 < coins[idx + 1]:
                total = total * 2 + 1
                ans += 1
            if total + 1 == coins[idx + 1] == coins[L] and coins[L] != coins[L -1]:
                ans += 1

            idx += 1
        return ans


coins = [1,4,10]
target = 19

coins = [1,4,10,5,7,19]
target = 19

coins = [1,1,1]
target = 20

coins = [1,1,1,5,10]
target = 100000

coins = [100000]
target = 100000

coins = [2]
target = 5

coins = [15,1,12]
target = 43

solution = Solution()
print(solution.minimumAddedCoins(coins, target))
