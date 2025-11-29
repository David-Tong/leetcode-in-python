class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        # pre-process
        nums = set(nums)

        # process
        target = original
        while target in nums:
            target *= 2
        return target


nums = [5,3,6,1,12]
original = 3

nums = [2,7,9]
original = 4

solution = Solution()
print(solution.findFinalValue(nums, original))
