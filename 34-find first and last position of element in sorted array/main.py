class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        # search the first position
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        low = -1
        if nums[left] == target:
            low = left
        elif nums[right] == target:
            low = right

        # search the last position
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle - 1

        high = -1
        if nums[right] == target:
            high = right
        elif nums[left] == target:
            high = left

        return [low, high]


nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = []
target = 0

nums = [1]
target = 1

nums = [5,6,8,8,8,8,8,8,8,8,8,10,11]
target = 8

solution = Solution()
print(solution.searchRange(nums, target))
