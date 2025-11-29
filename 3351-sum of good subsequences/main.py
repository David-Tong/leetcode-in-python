class Solution(object):
    def sumOfGoodSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        # dp init
        # dp[x] - the sum of good subsequences ended with num x
        # counts[x] - the number of good subsequences ended with num x
        from collections import defaultdict
        dp = defaultdict(int)
        counts = defaultdict(int)

        # dp transfer
        for num in nums:
            if num - 1 in dp:
                dp[num] = (dp[num] + dp[num - 1] + counts[num - 1] * num) % MODULO
                counts[num] += counts[num - 1]
            if num + 1 in dp:
                dp[num] = (dp[num] + dp[num + 1] + counts[num + 1] * num) % MODULO
                counts[num] += counts[num + 1]
            dp[num] = (dp[num] + num) % MODULO
            counts[num] += 1

        # print(dp)
        # print(counts)

        ans = sum(dp.values()) % MODULO
        return ans


nums = [1,2,1]
nums = [3,4,5]

from random import randint
nums = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.sumOfGoodSubsequences(nums))
