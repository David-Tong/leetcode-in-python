class Solution(object):
    def twoSum(self, nums, target):
        def getIndexByValFromLeft(nums, val):
            index = 0
            while index < len(nums):
                if nums[index] == val:
                    return index
                index += 1

        def getIndexByValFromRight(nums, val):
            index = len(nums) - 1
            while index >= 0:
                if nums[index] == val:
                    return index
                index -= 1

        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums) - 1
        while left < right:
            addon = sorted_nums[left] + sorted_nums[right]
            if addon == target:
                return getIndexByValFromLeft(nums, sorted_nums[left]), getIndexByValFromRight(nums, sorted_nums[right])
            elif addon > target:
                right -= 1
            elif addon < target:
                left += 1


nums = [2, 7, 11, 15]
target = 9

#nums = [3, 2, 4]
#target = 6

#nums = [3, 3]
#target = 6

solution = Solution()
print(solution.twoSum(nums, target))