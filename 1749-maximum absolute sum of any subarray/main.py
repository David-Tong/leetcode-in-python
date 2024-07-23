class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # init
        # dp[x][0] - maxi sum till nums[x]
        # dp[x][1] - mini sum till nums[x]
        L = len(nums)
        dp = [[0] * 2 for _ in range(L)]

        # dp
        for x in range(L):
            if x == 0:
                dp[x][0] = nums[x]
                dp[x][1] = nums[x]
            else:
                dp[x][0] = max(0, max(nums[x], max(dp[x - 1][0] + nums[x], dp[x - 1][1] + nums[x])))
                dp[x][1] = min(0, min(nums[x], min(dp[x - 1][0] + nums[x], dp[x - 1][1] + nums[x])))

        print(dp)
        ans = 0
        for x in range(L):
            ans = max(ans,max(abs(dp[x][0]), abs(dp[x][1])))
        return ans


nums = [1,-3,2,3,-4]
nums = [2,-5,1,-4,3,-2]

solution = Solution()
print(solution.maxAbsoluteSum(nums))
