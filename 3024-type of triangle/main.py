class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # pre-process
        nums = sorted(nums)

        # process
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"


nums = [3,3,3]
nums = [3,4,5]

solution = Solution()
print(solution.triangleType(nums))
