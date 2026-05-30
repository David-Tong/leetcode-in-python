class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        misplaceds = list()

        idx = 0
        while idx < L:
            if nums[idx] != idx:
                misplaceds.append(nums[idx])
            idx += 1

        # process
        if len(misplaceds) > 0:
            ans = misplaceds[0]
            for misplaced in misplaceds[1:]:
                ans &= misplaced
            return ans
        else:
            return 0


nums = [0,3,2,1]
nums = [0,1,3,2]
nums = [3,2,1,0]

import random
nums = [_ for _ in range(10 ** 5)]
random.shuffle(nums)
print(nums)

"""
import random
nums = [_ for _ in range(10 ** 5)]
random.shuffle(nums)
print(nums)
"""
nums = [3,1,0,2]

solution = Solution()
print(solution.sortPermutation(nums))
