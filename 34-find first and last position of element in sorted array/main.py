class Solution:
    def searchRange(self, nums, target):
        def binarySearchRight(nums, target):
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                middle = (left + right) // 2
                if nums[middle] <= target:
                    left = middle
                else:
                    right = middle

            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return -1

        def binarySearchLeft(nums, target):
            left = 0
            right = len(nums) - 1
            while left + 1 < right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle
                else:
                    right = middle

            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1

        if len(nums) == 0:
            return -1, -1
        return binarySearchLeft(nums, target), binarySearchRight(nums, target)

nums = [5, 7, 7, 8, 8, 10]
target = 6

#nums = [1, 2, 3]
#target = 3

nums = []
target = 0

sol = Solution()
print(sol.searchRange(nums, target))
