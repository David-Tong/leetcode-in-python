class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle
            elif nums[middle] > target:
                right = middle
            else:
                return middle

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

nums = [-1, 0, 3, 5, 9, 12]
target = -1

nums = [1]
target = 1

solution = Solution()
print(solution.search(nums, target))
