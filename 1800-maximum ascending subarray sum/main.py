class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        total = nums[0]
        for x in range(L - 1):
            if nums[x] < nums[x + 1]:
                total += nums[x + 1]
            else:
                ans = max(ans, total)
                total = nums[x + 1]
        ans = max(ans, total)
        return ans


nums = [10,20,30,5,10,50]
"""
nums = [10,20,30,40,50]
nums = [12,17,15,13,10,11,12]
nums = [100,10,1]
"""

solution = Solution()
print(solution.maxAscendingSum(nums))
