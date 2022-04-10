class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for x in range(1, len(nums)):
            if x < 2:
                dp[x] = max(dp[x-1], nums[x])
            else:
                dp[x] = max(dp[x - 1], max(dp[:x - 1]) + nums[x])

        return max(dp)


nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
nums = [2, 1, 1, 2]
nums = [1]
nums = [2, 1]

solution = Solution()
print(solution.rob(nums))