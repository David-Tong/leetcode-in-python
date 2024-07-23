class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        mini = float("inf")
        mini2 = float("inf")

        for price in prices:
            if price < mini:
                mini2 = mini
                mini = price
            elif price < mini2:
                mini2 = price

        if money >= mini + mini2:
            return money - mini - mini2
        else:
            return money


prices = [1,2,2]
money = 3

prices = [15,13,9,8,7,6,5,4,3,2,1]
money = 3

solution = Solution()
print(solution.buyChoco(prices, money))
