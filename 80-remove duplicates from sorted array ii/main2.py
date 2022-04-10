class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def removeKDuplicates(nums, k):
            if len(nums) <= k:
                return len(nums)

            slow = k
            fast = k
            while fast < len(nums):
                if nums[fast] != nums[slow - k]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1
            return slow

        return removeKDuplicates(nums, 2)


nums = [1, 1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
nums = [1, 1, 1, 1, 1, 2, 3, 5, 5, 5, 5, 5, 5]
nums = [1, 1, 1]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
