class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        dp = [False] * (L + 1)
        dp[0] = True

        for x in range(1, L):
            # case 1
            if dp[x - 1]:
                if nums[x] == nums[x - 1]:
                    dp[x + 1] = True
            # case 2, 3
            if x >= 2 and dp[x - 2]:
                if nums[x] == nums[x - 1] == nums[x - 2]:
                    dp[x + 1] = True
                if nums[x] - nums[x - 1] == 1 and nums[x - 1] - nums[x - 2] == 1:
                    dp[x + 1] = True

        return dp[L]


nums = [4,4,4,5,6]
nums = [1,1,1,2]
nums = [1,1]
nums = [803201,803201,803201,803201,803202,803203]

solution = Solution()
print(solution.validPartition(nums))

