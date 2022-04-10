class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def doSearch(left, right, nums, target):
            if left > right:
                return False
            else:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return True
                if nums[left] == target:
                    return True
                if nums[right] == target:
                    return True
                found = False
                if nums[left] <= nums[middle]:
                    if nums[left] < target < nums[middle]:
                        found |= doSearch(left, middle - 1, nums, target)
                    else:
                        found |= doSearch(middle + 1, right, nums, target)
                if nums[middle] <= nums[right]:
                    if nums[middle] < target < nums[right]:
                        found |= doSearch(middle + 1, right, nums, target)
                    else:
                        found |= doSearch(left, middle - 1, nums, target)
                return found
        return doSearch(0, len(nums) - 1, nums, target)


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
#target = 3

#nums = [3, 5, 1]
#target = 3

#nums = [5, 1, 3]
#target = 3

#nums = [5, 1, 2, 3, 4]
#target = 1

#nums = [1, 0, 1, 1, 1]
#target = 0

solution = Solution()
print(solution.search(nums, target))
