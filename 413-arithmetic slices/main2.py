class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countSlices(slice):
            count = 0
            for x in range(3, slice + 1):
                count += (slice - x + 1)
            return count

        N = len(nums)
        if N < 3:
            return 0

        # dp[][0] the number of consecutive items with same difference
        # dp[][1] the difference
        dp = [[0] * 2 for x in range(N)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[1][0] = 2
        dp[1][1] = nums[1] - nums[0]

        slices = []
        for x in range(2, N):
            if nums[x] - nums[x-1] == dp[x-1][1]:
                dp[x][0] = dp[x-1][0] + 1
                dp[x][1] = dp[x-1][1]
            else:
                if dp[x-1][0] >= 3:
                    slices.append(dp[x-1][0])
                dp[x][0] = 2
                dp[x][1] = nums[x] - nums[x-1]
        if dp[x][0] >= 3:
            slices.append(dp[x][0])

        ans = 0
        for slice in slices:
            ans += countSlices(slice)
        return ans


nums = [1, 2, 3, 4]
nums = [1]
nums = [1, 2, 3, 4, 5, 3, 1, -1, 0, 1, 2]

solution = Solution()
print(solution.numberOfArithmeticSlices(nums))
