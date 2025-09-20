class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        processed = list()
        start = False
        count = 0
        for num in nums:
            if num == 1:
                if not start:
                    start = True
                    count = 1
                else:
                    processed.append(count)
                    count = 1
            else:
                count += 1
        # print(processed)

        # process
        # conner case:
        if not start:
            return 0
        if len(processed) == 0:
            return 1

        ans = 0
        if len(processed) > 0:
            ans = processed[0]
            for process in processed[1:]:
                ans = ans * process % MODULO
        return ans


nums = [0,1,0,0,1]
"""
nums = [0,1,0]
nums = [0,1,0,0,1,0,0,1]
nums = [0,1,0,0,1,0,0,1,0,1]
nums = [0,0,0]
"""

from random import randint
nums = [randint(0, 1) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.numberOfGoodSubarraySplits(nums))
