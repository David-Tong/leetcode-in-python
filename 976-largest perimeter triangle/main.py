class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        x = len(nums) - 3
        while x >= 0:
            if nums[x] + nums[x+1] > nums[x+2]:
                return nums[x] + nums[x+1] + nums[x+2]
            x -= 1
        return 0


nums = [2, 1, 2]
nums = [1, 2, 1]

solution = Solution()
print(solution.largestPerimeter(nums))
