class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1

        while left < len(nums):
            nums[left] = 0
            left += 1

        return nums


solution = Solution()

nums = [0, 1, 0, 3, 12]
nums = [0]
nums = [0, 0, 0, 0, 12, 13, 18, 0, 0, 0, 1, 2]
print(solution.moveZeroes(nums))
