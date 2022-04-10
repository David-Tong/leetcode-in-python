class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        for x in range(1, N):
            dp[x] = max(0, dp[x-1]) + nums[x]
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1]
nums = [5, 4, -1, 7, 8]

solution = Solution()
print(solution.maxSubArray(nums))
