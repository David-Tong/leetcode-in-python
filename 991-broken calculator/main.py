class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        count = 0
        while target > startValue:
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
            count += 1
        return count + startValue - target


startValue = 2
target = 3

startValue = 5
target = 8

startValue = 3
target = 10

solution = Solution()
print(solution.brokenCalc(startValue, target))
