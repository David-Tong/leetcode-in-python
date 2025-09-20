class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        evens, odds = defaultdict(int), defaultdict(int)
        even, odd = L, L
        for idx, num in enumerate(nums):
            evens[idx], odds[idx] = even, odd
            if num % 2 == 0:
                even = idx
            else:
                odd = idx
        # print(evens, odds)

        # process
        # dp init
        # dp[x] - maximize score after visit nums[:x+1]
        dp = [0] * (L + 1)
        dp[0] = nums[0]
        dp[L] = float("-inf")

        # dp transfer
        # dp[x] = max(dp[prev odd], dp[prev even]) after subtracting lose score x
        for idx in range(1, L):
            # even
            if nums[idx] % 2 == 0:
                dp[idx] = max(dp[odds[idx]] - x, dp[evens[idx]]) + nums[idx]
            # odd
            else:
                dp[idx] = max(dp[odds[idx]], dp[evens[idx]] - x) + nums[idx]
        # print(dp)

        ans = max(dp)
        return ans


nums = [2,3,6,1,9,2]
x = 5

nums = [2,4,6,8]
x = 3

from random import randint
nums = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
print(nums)
x = 1500

solution = Solution()
print(solution.maxScore(nums, x))
