class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [len(nums) + 1] * len(nums)
        dp[0] = 0
        for idx, num in enumerate(nums):
            for x in range(nums[idx]):
                if idx + x + 1 < len(nums):
                    dp[idx + x + 1] = min(dp[idx + x + 1], dp[idx] + 1)
        return dp[len(nums) - 1]


nums = [2, 3, 1, 1, 4]
nums = [2, 3, 0, 1, 4]
nums = [3]

nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]


solution = Solution()
print(solution.jump(nums))
