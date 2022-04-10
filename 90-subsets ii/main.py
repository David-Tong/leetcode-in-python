class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.anses = []

        def doSubset(nums, index, selected, unselected):
            if index == len(nums):
                self.anses.append(selected)
            else:
                if nums[index] not in unselected:
                    doSubset(nums, index + 1, selected[:] + [nums[index]], unselected[:])
                doSubset(nums, index + 1, selected[:], unselected[:] + [nums[index]])

        doSubset(nums, 0, [], [])
        return self.anses


nums = [1, 2, 2]
nums = [0]

solution = Solution()
print(solution.subsetsWithDup(nums))
