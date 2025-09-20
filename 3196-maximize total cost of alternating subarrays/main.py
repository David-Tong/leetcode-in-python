class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp init
        L = len(nums)
        dp = [0] * (L + 1)
        dp[0] = 0
        dp[1] = nums[0]

        # dp transfer
        # dp[x] = max(dp[x - 1] + nums[x], dp[x - 2] + nums[x - 1] - nums[x])
        for x in range(1, L):
            dp[x + 1] = max(dp[x] + nums[x], dp[x - 1] + nums[x - 1] - nums[x])
        # print(dp)
        ans = dp[L]
        return ans


nums = [1,-2,3,4]
nums = [1,-1,1,-1]
nums = [0]
nums = [1,-1]

from random import randint
nums = [randint(-100000, 100000) for _ in range(3 * 10 ** 4)]
print(nums)

solution = Solution()
print(solution.maximumTotalCost(nums))
