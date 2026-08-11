class Solution(object):
    def rob(self, nums, colors):
        """
        :type nums: List[int]
        :type colors: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        # dp init
        # dp[x][0] - the maximum amount of money you can rob, without robbing the xth house
        # dp[x][1] - the maximum amount of money you can rob, with robbing the xth house
        dp = [[0] * 2 for _ in range(L)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        # dp transfer
        # dp[x][0] = max(dp[x - 1][0], dp[x - 1][1])
        # dp[x][1] = max(dp[x - 1][0] + nums[x], dp[x - 1][1] + nums[x]) if colors[x - 1] != colors[x]
        for x in range(1, L):
            dp[x][0] = max(dp[x - 1][0], dp[x - 1][1])
            dp[x][1] = dp[x - 1][0] + nums[x]
            if colors[x - 1] != colors[x]:
                dp[x][1] = max(dp[x][1], dp[x - 1][1] + nums[x])

        # post-process
        ans = max(dp[L - 1][0], dp[L - 1][1])
        return ans


nums = [1,4,3,5]
colors = [1,1,2,2]

nums = [3,1,2,4]
colors = [2,3,2,2]

nums = [10, 1, 3, 9]
colors = [1, 1, 1, 2]

from random import randint
nums = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
colors = [randint(1, 10 ** 2) for _ in range(10 ** 4)]
print(nums)
print(colors)

solution = Solution()
print(solution.rob(nums, colors))