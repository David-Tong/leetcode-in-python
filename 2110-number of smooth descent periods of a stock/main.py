class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def numberOfPeriods(period):
            return (period * (period + 1)) // 2

        L = len(prices)

        periods = list()
        period = 1
        for x in range(1, L):
            if prices[x - 1] - prices[x] == 1:
                period += 1
            else:
                periods.append(period)
                period = 1
        periods.append(period)

        ans = 0
        for period in periods:
            ans += numberOfPeriods(period)
        return ans


prices = [3,2,1,4]
prices = [8,6,7,7]
prices = [1]
prices = [100,99,98,97,96,95,96,95,95,93,92,90]

solution = Solution()
print(solution.getDescentPeriods(prices))
