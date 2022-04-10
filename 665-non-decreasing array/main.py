class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for idx, num in enumerate(nums):
            if idx > 0:
                if nums[idx - 1] > nums[idx]:
                    count += 1
                    # make nums[idx] larger
                    if idx + 1 < len(nums) and nums[idx - 1] > nums[idx + 1]:
                        # or make nums[idx - 1] smaller
                        if idx - 2 >= 0 and nums[idx - 2] > nums[idx]:
                            return False
        if count > 1:
            return False
        else:
            return True


nums = [4, 2, 3]
nums = [4, 2, 1]
nums = [3, 4, 2, 3]
nums = [1]

solution = Solution()
print(solution.checkPossibility(nums))
