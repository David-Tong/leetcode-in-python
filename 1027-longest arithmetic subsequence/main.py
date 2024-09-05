class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        # dp[x][y] - the longest subsequence length for xth element for y difference
        from collections import defaultdict
        dp = list()
        for x in range(L):
            dp.append(defaultdict(int))

        ans = 0
        for x in range(1, L):
            for y in range(x):
                difference = nums[x] - nums[y]
                if difference in dp[y]:
                    dp[x][difference] = dp[y][difference] + 1
                else:
                    dp[x][difference] = 2
                ans = max(ans, dp[x][difference])
        return ans


nums = [3,6,9,12]
nums = [9,4,7,2,10]
nums = [20,1,15,3,10,5,8]
nums = [3,6]
nums = [5,4,3,2,1,2,3,4,5,6]

solution = Solution()
print(solution.longestArithSeqLength(nums))
