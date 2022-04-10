class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        nums = sorted(nums)
        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                return True
            index += 1
        return False
