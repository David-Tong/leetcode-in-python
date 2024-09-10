class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def canDivide(target, nums, threshold):
            from math import ceil
            total = 0
            for num in nums:
                total += ceil(num * 1.0 / target)
            if total <= threshold:
                return True
            else:
                return False

        left = 1
        right = max(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if canDivide(middle, nums, threshold):
                right = middle
            else:
                left = middle + 1

        if canDivide(left, nums, threshold):
            return left
        else:
            return right


nums = [1,2,5,9]
threshold = 6

nums = [44,22,33,11,1]
threshold = 5

nums = [90]
threshold = 1

solution = Solution()
print(solution.smallestDivisor(nums, threshold))
