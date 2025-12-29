class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        L = len(nums)
        from collections import defaultdict
        rights = defaultdict(int)
        for num in nums:
            rights[num] += 1

        # process
        lefts = defaultdict(int)
        rights[nums[0]] -= 1
        ans = 0

        for x in range(1, L - 1):
            lefts[nums[x - 1]] += 1
            rights[nums[x]] -= 1
            target = nums[x] * 2
            ans += lefts[target] * rights[target] % MODULO
        ans = ans % MODULO
        return ans


nums = [6,3,6]
nums = [0,1,0,0]
# nums = [8,4,2,8,4]

"""
import random
nums = [random.choice([2, 4, 8]) for _ in range(10 ** 5)]
print(nums)
"""

solution = Solution()
print(solution.specialTriplets(nums))
