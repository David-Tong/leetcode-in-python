class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nums = sorted(nums)
        dp = [[] for _ in range(N)]
        ans = []
        for idx, num in enumerate(nums):
            dp[idx] = [num]
            for idx2, num2 in enumerate(nums[:idx]):
                if num % num2 == 0:
                    if len(dp[idx2]) + 1 > len(dp[idx]):
                        dp[idx] = dp[idx2] + [num]
            if len(dp[idx]) > len(ans):
                ans = dp[idx][:]
        return ans


nums = [1,2,3]
nums = [1,2,4,8]
nums = [1,2,4,12]
nums = [1]
nums = [1,2,4,8,16,3,6,12,15,24,30]

solution = Solution()
print(solution.largestDivisibleSubset(nums))
