class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = 0
        for x in range(1, L):
            if nums[x] <= nums[x - 1]:
                ans += nums[x - 1] + 1 - nums[x]
                nums[x] = nums[x - 1] + 1
        return ans


nums = [1,2,2]
nums = [3,2,1,2,1,7]

solution = Solution()
print(solution.minIncrementForUnique(nums))
