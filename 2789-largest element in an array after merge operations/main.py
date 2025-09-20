class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        nums = nums[::-1]

        # process
        stack = list()
        for num in nums:
            merged = num
            while stack and merged <= stack[-1]:
                merged += stack.pop()
            stack.append(merged)

        # print(stack)
        ans = max(stack)
        return ans


nums = [2,3,7,9,3]
nums = [5,3,3]

from random import randint
nums = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxArrayValue(nums))
