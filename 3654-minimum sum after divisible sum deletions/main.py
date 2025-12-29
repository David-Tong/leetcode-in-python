class Solution(object):
    def minArraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        # dp init
        # dp[x] - the minimum sum after divisible sum deletions for nums[:x + 1]
        dp = [0] * L

        # dp transfer
        for x in range(L):
            mod = presums[x + 1] % k
            if mod == 0:
                dp[x] = 0
            else:
                if x == 0:
                    dp[x] = nums[x]
                else:
                    if mod in dicts:
                        dp[x] = min(dp[x - 1] + nums[x], dicts[mod])
                    else:
                        dp[x] = dp[x - 1] + nums[x]
            if mod not in dicts:
                dicts[mod] = dp[x]
            else:
                dicts[mod] = min(dicts[mod], dp[x])

        ans = dp[L - 1]
        return ans


nums = [1,1,1]
k = 2

nums = [3, 1, 4, 1, 5]
k = 3

nums = [193, 951, 145, 92, 205, 751, 631, 691, 206, 902]
k = 5

nums = [1,1,2,1,1]
k = 3

"""
from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 4)]
k = 10 ** 3
print(nums)
"""

solution = Solution()
print(solution.minArraySum(nums, k))
