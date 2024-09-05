class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


nums = [5,6,2,7,4]
nums = [4,2,5,9,7,4,8]

solution = Solution()
print(solution.maxProductDifference(nums))
