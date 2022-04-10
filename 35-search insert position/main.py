class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle
            else:
                return middle

        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:
            return len(nums)


nums = [1, 3, 5, 6]
target = 5

nums = [1, 3, 5, 6]
target = 2

nums = [1, 3, 5, 6]
target = 7

#nums = [1, 3, 5, 6]
#target = 0

solution = Solution()
print(solution.searchInsert(nums, target))
