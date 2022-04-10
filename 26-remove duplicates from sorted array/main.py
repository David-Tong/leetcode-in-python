class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        slow = 0
        fast = 1
        while fast < N:
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1]
nums = [1, 2, 3, 4, 5, 5]

solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
