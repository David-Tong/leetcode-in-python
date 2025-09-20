class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # pre-process
        L = len(nums)

        presums = [0]
        for x in range(L):
            presums.append(presums[-1] + nums[x])

        # dp init
        # dp[x][y] - the largest sum of averages for nums[:x] with k non-empty adjacent subarrays
        dp = [[float("-inf")] * (k + 1) for _ in range(L + 1)]
        dp[0][0] = 0

        # dp transfer
        # dp[x][y] - dp[k][y - 1] for k in 0 ... x - 1
        for x in range(1, L + 1):
            for y in range(0, k):
                for z in range(x):
                    dp[x][y + 1] = max(dp[x][y + 1], dp[z][y] + (presums[x] - presums[z]) * 1.0 / (x - z))
        # print(dp)

        ans = dp[L][k]
        return ans


nums = [9,1,2,3,9]
k = 3

nums = [1,2,3,4,5,6,7]
k = 4

from random import randint
nums = [randint(1, 10 ** 4) for _ in range(100)]
print(nums)
k = 100

solution = Solution()
print(solution.largestSumOfAverages(nums, k))
