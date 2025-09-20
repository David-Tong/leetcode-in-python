class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # process
        from collections import defaultdict
        dicts = defaultdict(list)
        presums = list()
        presums.append(0)
        ans = float("-inf")
        for idx, num in enumerate(nums):
            presums.append(presums[-1] + num)
            target = num + k
            if target in dicts:
                ans = max(ans, presums[idx + 1] - dicts[target])
            target = num - k
            if target in dicts:
                ans = max(ans, presums[idx + 1] - dicts[target])
            dicts[num] = min(dicts[num], presums[idx])

        return 0 if ans == float("-inf") else ans


nums = [1,2,3,4,5,6]
k = 1

nums = [-1,3,2,4,5]
k = 3

nums = [-1,-2,-3,-4]
k = 2

"""
from random import randint
nums = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
k = 10 ** 6

print(nums)
"""

solution = Solution()
print(solution.maximumSubarraySum(nums, k))
