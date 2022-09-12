class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        total = sum(nums)
        # dp[x] - rotate function value when nums[0] * x and nums[1] * (x + 1)
        dp = [0] * N
        for x in range(N):
            dp[0] += nums[x] * x

        idx = N - 1
        for x in range(1, N):
            dp[x] = dp[x-1] + total - N * nums[idx]
            idx -= 1

        return max(dp)


nums = [4,3,2,6]
nums = [100]
nums = [100,12,-100,66,23]

solution = Solution()
print(solution.maxRotateFunction(nums))
