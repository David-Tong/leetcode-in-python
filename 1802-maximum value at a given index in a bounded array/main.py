class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def getSum(target, items):
            if items == 0:
                return 0

            if target - items > 0:
                return (target - 1) * target // 2 - (target - items - 1) * (target - items) // 2
            else:
                return (target - 1) * target // 2 + items - (target - 1)

        def canPlace(target):
            # place
            total = getSum(target, index) + getSum(target, n - index - 1) + target
            # check
            if total <= maxSum:
                return True
            else:
                return False

        left = 1
        right = maxSum

        while left + 1 < right:
            middle = (left + right) // 2
            if canPlace(middle):
                left = middle
            else:
                right = middle - 1

        if canPlace(right):
            return right
        else:
            return left


n = 4
index = 2
maxSum = 6

n = 6
index = 1
maxSum = 10

n = 1
index = 0
maxSum = 100

n = 8257285
index = 4828516
maxSum = 850015631

n = 3
index = 2
maxSum = 18

solution = Solution()
print(solution.maxValue(n, index, maxSum))
