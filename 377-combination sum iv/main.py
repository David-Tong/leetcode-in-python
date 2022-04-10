class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = target + 1
        dp = [0] * N
        for num in nums:
            if num < N:
                dp[num] = 1

        for x in range(N):
            for num in nums:
                if x > num:
                    dp[x] += dp[x - num]
        return dp[N-1]


nums = [1, 2, 3]
target = 4

nums = [9]
target = 3

solution = Solution()
print(solution.combinationSum4(nums, target))
