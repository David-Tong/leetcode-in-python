class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        nums[0] -= k
        idx = 1
        duplicated = 0
        while idx < L:
            nums[idx] = min(max(nums[idx - 1] + 1, nums[idx] - k), nums[idx] + k)
            if nums[idx] == nums[idx - 1]:
                duplicated += 1
            idx += 1
        ans = L - duplicated
        return ans


nums = [1,2,2,3,3,4]
k = 2

nums = [4,4,4,4]
k = 1

"""
from random import randint
nums = [randint(1, 10 ** 2) for _ in range(10 ** 5)]
print(nums)
k = 5
"""

nums = [56,56,54,54]
k = 0

nums = [10,10,10,5,10]
k = 1

solution = Solution()
print(solution.maxDistinctElements(nums, k))
