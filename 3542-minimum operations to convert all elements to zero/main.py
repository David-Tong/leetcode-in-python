class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        stack = list()
        ans = 0
        for num in nums:
            s = set()
            while stack and stack[-1] > num:
                s.add(stack.pop())
            if num > 0:
                stack.append(num)
            ans += len(s)
        s = set()
        while stack:
            s.add(stack.pop())
        ans += len(s)
        return ans


nums = [0,2]
nums = [3,1,2,1]
nums = [1,2,1,2,1,2]
nums = [7,2,0,4,2]

"""
from random import randint
nums = [randint(0, 10 ** 5) for _ in range(10 ** 3)]
print(nums)
"""

solution = Solution()
print(solution.minOperations(nums))
