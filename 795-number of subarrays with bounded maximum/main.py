class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        def numSubarrayLessThanK(nums, k):
            total = 0
            count = 0
            for num in nums:
                if num <= k:
                    count += 1
                else:
                    count = 0
                total += count
            return total

        return numSubarrayLessThanK(nums, right) - numSubarrayLessThanK(nums, left - 1)


nums = [2,1,4,3]
left = 2
right = 3

nums = [2,9,2,5,6]
left = 2
right = 8

solution = Solution()
print(solution.numSubarrayBoundedMax(nums, left, right))
