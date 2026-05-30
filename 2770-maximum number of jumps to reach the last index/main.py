class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        # dp init
        # dp[x] - the maximum number of jumps to reach x
        dp = [float('-inf')] * L
        dp[0] = 0

        # dp transfer
        # dp[x] = max(dp[y] + 1) for all y < x and abs(nums[x] - nums[y]) <= target
        for x in range(L):
            for y in range(x):
                if abs(nums[x] - nums[y]) <= target:
                    dp[x] = max(dp[x], dp[y] + 1)
        # print(dp)

        # post-process
        ans = -1 if dp[L - 1] == float('-inf') else dp[L - 1]
        return ans


nums = [1,3,6,4,1,2]
target = 2

"""
nums = [1,3,6,4,1,2]
target = 3

nums = [1,3,6,4,1,2]
target = 0

nums = [0,2,1,3]
target = 1
"""

"""
from random import randint
nums = [randint(-10 ** 3, 10 ** 3) for _ in range(10 ** 3)]
target = 500
print(nums)
"""

solution = Solution()
print(solution.maximumJumps(nums, target))
