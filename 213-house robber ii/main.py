class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[] if not rob house 1, dp2[] if rob house 1
        dp = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp[0] = 0
        dp2[0] = nums[0]
        for x in range(1, len(nums)):
            if x < 2:
                dp[x] = nums[1]
                dp2[x] = nums[0]
            else:
                dp[x] = max(dp[x - 1], nums[x] + max(dp[:x - 1]))
                if x < len(nums) - 1:
                    dp2[x] = max(dp2[x-1], nums[x] + max(dp2[:x-1]))
        return max(dp[len(nums) - 1], dp2[len(nums) - 2])


nums = [2, 3, 2]
nums = [1, 2, 3, 1]
nums = [1, 2, 3]
nums = [100]
nums = [100, 5, 55]

solution = Solution()
print(solution.rob(nums))
