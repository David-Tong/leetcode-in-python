class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while slow == 0 or slow != fast:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

        slow = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow


nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]
nums = [2, 2, 2, 2, 2]
nums = [1, 1]
nums = [3, 1, 3, 4, 2]
nums = [4, 1, 3, 4, 2]

solution = Solution()
print(solution.findDuplicate(nums))
