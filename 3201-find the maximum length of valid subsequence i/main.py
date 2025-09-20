class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp init
        # dp[x][y] - the maximum length of valid subsequence in nums[:x + 1]
        #          - and (sub[x] + sub[x - 1]) % 2 == y
        L = len(nums)
        dp = [[1] * 2 for _ in range(L)]
        last = [-1] * 2

        # dp transfer
        # dp[x][y] = dp[last[d]][y] + 1
        # d = (y - nums[x] % 2 + 2) % 2
        MOD = 2
        ans = 0
        for x in range(L):
            for y in range(MOD):
                d = (y - nums[x] % MOD + MOD) % MOD
                if last[d] >= 0:
                    dp[x][y] = dp[last[d]][y] + 1
                    ans = max(ans, dp[x][y])
            last[nums[x] % MOD] = x
        return ans


nums = [1,2,3,4]
nums = [1,2,1,1,2,1,2]
nums = [1,3]
nums = [1] * 10 + [2] * 10
nums = [1,1,2,2]

solution = Solution()
print(solution.maximumLength(nums))
