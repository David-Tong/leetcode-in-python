class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        ans = total
        while total >= numExchange:
            quotient = total // numExchange
            residual = total % numExchange
            ans += quotient
            total = quotient + residual
        return ans


numBottles = 9
numExchange = 3

numBottles = 15
numExchange = 4

numBottles = 100
numExchange = 33

solution = Solution()
print(solution.numWaterBottles(numBottles, numExchange))
