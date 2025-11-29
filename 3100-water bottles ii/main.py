class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # process
        ans = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            ans += 1
            empty_bottles = empty_bottles - numExchange + 1
            numExchange += 1
        return ans


numBottles = 13
numExchange = 6

numBottles = 10
numExchange = 3

solution = Solution()
print(solution.maxBottlesDrunk(numBottles, numExchange))
