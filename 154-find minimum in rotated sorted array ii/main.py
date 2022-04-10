class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def doFind(nums, left, right):
            mini = float("inf")
            if left + 1 < right:
                middle = (left + right) // 2
                if nums[left] >= nums[middle]:
                    mini = min(mini, doFind(nums, left, middle))
                if nums[middle] >= nums[right]:
                    mini = min(mini, doFind(nums, middle, right))
            return min(mini, min(nums[left], nums[right]))
        return doFind(nums, 0, len(nums) - 1)


nums = [1,3,5]
nums = [2,2,2,0,1]
nums = [5,3,1]
nums = [0,0,0,0,0]

solution = Solution()
print(solution.findMin(nums))
