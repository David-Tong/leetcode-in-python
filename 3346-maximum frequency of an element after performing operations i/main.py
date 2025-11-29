class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        # pre-process
        nums = sorted(nums)
        from collections import defaultdict
        dicts = defaultdict(int)
        for num in nums:
            dicts[num] += 1

        # process
        from bisect import bisect_left, bisect_right
        left, right = min(nums), max(nums) + 1
        ans = 0
        for x in range(left, right):
            idx = bisect_left(nums, x - k)
            idx2 = bisect_right(nums, x + k)
            ans = max(ans, min(numOperations, idx2 - idx - dicts[x]) + dicts[x])
            # print(x, min(numOperations, idx2 - idx - dicts[x]) + dicts[x])
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
