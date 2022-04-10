class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if middle % 2 == 1:
                if nums[middle] == nums[middle - 1]:
                    left = middle
                else:
                    right = middle
            else:
                if nums[middle] == nums[middle + 1]:
                    left = middle
                else:
                    right = middle

        if left % 2 == 1:
            if nums[left] == nums[left - 1]:
                return nums[right]
            else:
                return nums[left]
        else:
            if nums[left] != nums[right]:
                return nums[left]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
#nums = [3, 3, 7, 7, 10, 11, 11]
#nums = [1]
#nums = [1, 1, 2]
#nums = [1, 2, 2]

solution = Solution()
print(solution.singleNonDuplicate(nums))
