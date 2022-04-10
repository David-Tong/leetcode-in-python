class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L == 0:
            return 0
        dp = [1] * L

        for i in range(L):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 4]))
