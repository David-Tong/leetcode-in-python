class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        def getProfit(target, inventory, orders):
            profit = 0
            for invty in inventory:
                if invty > target:
                    profit += invty * (invty + 1) // 2 - target * (target + 1) // 2
                    orders -= (invty - target)
            profit += target * orders
            return profit

        def canSell(target, inventory, orders):
            for invty in inventory:
                if invty >= target:
                    orders -= (invty - target + 1)
                if orders <= 0:
                    return True
            return False

        MODULO = 10 ** 9 + 7

        left = 1
        right = max(inventory)

        while left + 1 < right:
            middle = (left + right) // 2
            if canSell(middle, inventory, orders):
                left = middle
            else:
                right = middle - 1

        if canSell(right, inventory, orders):
            print(right)
            ans = getProfit(right, inventory, orders)
        elif canSell(left, inventory, orders):
            print(left)
            ans = getProfit(left, inventory, orders)

        return ans % MODULO


inventory = [2,5]
orders = 4

#inventory = [3,5]
#orders = 6

#inventory = [1000000000]
#orders = 1000000000

#inventory = [3,5]
#orders = 6

inventory = [497978859,167261111,483575207,591815159]
orders = 836556809

solution = Solution()
print(solution.maxProfit(inventory, orders))
