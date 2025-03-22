class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        for x in range(0, L, 2):
            if nums[x] != nums[x + 1]:
                return False
        return True


nums = [3,2,3,2,2,2]
nums = [1,2,3,4]

solution = Solution()
print(solution.divideArray(nums))
