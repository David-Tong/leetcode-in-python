class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        stack = list()
        idx = 0
        while idx < L:
            # must be a valid sequence
            # len(stack) + L - idx > k
            while stack and len(stack) > k + idx - L and stack[-1] > nums[idx]:
                stack.pop()
            stack.append(nums[idx])
            idx += 1

        # post-process
        while len(stack) > k:
            stack.pop()
        ans = stack
        return ans


nums = [3,5,2,6]
k = 2

nums = [2,4,3,3,5,4,9,6]
k = 4

nums = [1,2,3,4,5,6,7]
k = 4

nums = [7,6,5,4,3,2,1]
k = 4

"""
from random import randint
nums = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
k = 10 ** 3
print(nums)
"""

solution = Solution()
print(solution.mostCompetitive(nums, k))
