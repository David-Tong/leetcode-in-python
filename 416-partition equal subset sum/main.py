class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            target = total // 2

        # dp[x][y] - the first x num can sum up y
        dp = [[False] * (target + 1) for _ in range(L + 1)]

        for x in range(1, L + 1):
            for y in range(target + 1):
                if y == 0:
                    dp[x][y] = True
                else:
                    if y - nums[x - 1] >= 0:
                        dp[x][y] = dp[x - 1][y - nums[x - 1]] or dp[x - 1][y]
                    else:
                        dp[x][y] = dp[x - 1][y]

        for x in range(1, L + 1):
            if dp[x][target]:
                return True
        return False


nums = [1,5,11,5]
nums = [1,2,3,5]
nums = [2,3,4,3,6]
nums = [14,9,8,4,3,2]
nums = [100]

solution = Solution()
print(solution.canPartition(nums))
