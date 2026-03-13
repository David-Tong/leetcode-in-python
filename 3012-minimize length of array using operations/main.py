class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        # rule 1 - if we may get a remainder less than the smallest num
        #        - then return 1
        idx = 1
        while idx < L:
            if nums[idx] % nums[0] != 0:
                return 1
            idx += 1

        # rule 2 - if we can't get remainder less than the smallest num
        #        - then return the number of the smallest num + 1 // 2
        idx = 0
        ans = 1
        while idx < L:
            if nums[idx] == nums[0]:
                ans += 1
            else:
                break
            idx += 1
        ans = ans // 2
        return ans


nums = [1,2,3]
nums = [1,4,3,1]
nums = [5,5,5,10,5]
nums = [2,3,4]
# nums = [4,4,4]

"""
from random import randint
nums = [randint(1, 10) for _ in range(10 ** 5)]
print(nums)
"""

solution = Solution()
print(solution.minimumArrayLength(nums))
