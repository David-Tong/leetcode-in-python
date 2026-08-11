class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        # pre-process
        L = len(nums)

        # prefix sums
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # helper function
        def good(left, right):
            return (right - left == 1) or (presum[right] - presum[left] >= m)

        # process
        # dp init
        # dp[left][right] means nums[left:right] can be split
        dp = [[False] * (L + 1) for _ in range(L + 1)]

        # base case: single element arrays are good
        for x in range(L):
            dp[x][x + 1] = True

        # dp transfer
        # process intervals by increasing length
        for length in range(2, L + 1):
            for left in range(0, L - length + 1):
                right = left + length

                # try all split points
                for k in range(left + 1, right):
                    if good(left, k) and good(k, right):
                        if dp[left][k] and dp[k][right]:
                            dp[left][right] = True
                            break

        return dp[0][L]


nums = [2, 2, 1]
m = 4

nums = [2, 1, 3]
m = 5

nums = [2, 3, 3, 2, 3]
m = 6

"""
from random import randint
nums = [randint(1, 100) for _ in range(100)]
m = 65
print(nums)
"""

nums = [38, 96, 25, 55, 62, 62, 58, 55, 4, 32, 35, 100, 12, 87, 16, 55, 16, 53, 77, 57, 44, 87, 23]
m = 143

nums = [98, 14, 47, 63, 5, 28, 9, 26, 26, 29, 51, 3, 79, 43, 49, 26, 85, 12, 53, 59, 20, 36, 79, 25, 60, 51, 65, 43, 69, 28, 92, 13, 81, 28, 29, 16, 86, 1, 58, 37, 16, 5, 23, 48, 21, 12, 94, 26, 99, 25, 61, 41, 71, 51, 17, 72, 10, 76, 13, 82, 18, 71, 2, 38, 6, 12, 65, 25, 11, 43, 78, 44, 66, 25, 98, 8, 47, 56, 1, 71, 2, 83, 15, 96, 5, 71, 44, 49, 25, 36, 68, 37, 23, 25, 42, 71, 52]
m = 127

solution = Solution()
print(solution.canSplitArray(nums, m))
