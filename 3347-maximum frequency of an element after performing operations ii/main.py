class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        counts = defaultdict(int)
        diffs = defaultdict(int)
        for num in nums:
            counts[num] += 1
            diffs[num]
            diffs[num - k] += 1
            diffs[num + k + 1] -= 1

        # process
        total = 0
        ans = 0
        for diff in sorted(diffs):
            total += diffs[diff]
            ans = max(ans, min(total, counts[diff] + numOperations))
        return ans


nums = [1,4,5]
k = 1
numOperations = 2

nums = [5,11,20,20]
k = 5
numOperations = 1

nums = [5,11,11,18,19,20,20,25,25,26]
k = 5
numOperations = 1

from random import randint
nums = [randint(1, 100) for _ in range(10 ** 5)]
# print(nums)
k = 5
numOperations = 3000

nums = [88,53]
k = 27
numOperations = 2

nums = [1,90]
k = 76
numOperations = 1

nums = [110,3,43,39]
k = 52
numOperations = 4


solution = Solution()
print(solution.maxFrequency(nums, k, numOperations))