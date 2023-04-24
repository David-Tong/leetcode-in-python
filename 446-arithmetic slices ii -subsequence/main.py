class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        # dp[x][y] - the number of sequence ended with nums[x] with difference of y
        from collections import defaultdict

        dp = list()
        for x in range(L):
            dp.append(defaultdict(int))

        ans = 0
        for x in range(L):
            for y in range(x):
                diff = nums[x] - nums[y]
                dp[x][diff] += dp[y][diff] + 1
                ans += dp[y][diff]
        return ans


nums = [2,4,6,8,10]
nums = [7,7,7,7,7]
nums = [2,4,6,8,10,14]
nums = [2,4,6,8,10,7,7,7,7,7,14]
nums = [1,2,1,2,4,1,5,10]
nums = [2,2,3,4]

solution = Solution()
print(solution.numberOfArithmeticSlices(nums))
