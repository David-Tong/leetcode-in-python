class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        dicts = defaultdict(list)
        spans = defaultdict(int)
        for idx, num in enumerate(nums):
            if num not in spans:
                spans[num] = L
            dicts[num].append(idx)
            if len(dicts[num]) >= 3:
                l = len(dicts[num]) - 1
                spans[num] = min(spans[num], dicts[num][l] - dicts[num][l - 2])
        # print(dicts)
        # print(spans)

        # process
        ans = float("inf")
        for key in dicts:
            if len(dicts[key]) >= 3:
                ans = min(ans, spans[key] * 2)
        return -1 if ans == float("inf") else ans


nums = [1,2,1,1,3]
nums = [1,1,2,3,2,1,2]
nums = [1]
nums = [4, 2, 1, 8, 9, 4, 8, 2, 8, 6, 1, 9, 3, 4, 1, 8, 9, 4, 3, 2, 3, 4, 8, 3, 1, 2, 6, 3, 8, 3, 1, 7, 7, 6, 10, 9, 8, 8, 1, 4, 9, 3, 10, 7, 2, 9, 8, 4, 8, 5, 6, 2, 3, 3, 6, 7, 4, 3, 5, 2, 4, 3, 6, 1, 9, 2, 6, 3, 7, 2, 7, 4, 7, 6, 1, 1, 1, 3, 7, 7, 10, 5, 10, 6, 8, 2, 10, 2, 6, 1, 10, 7, 9, 5, 4, 8, 9, 3, 8, 2]
nums = [1, 3, 2, 2, 3, 1, 2, 3, 3, 2, 3, 1, 1, 3, 3, 3, 3, 1, 3, 3]

"""
from random import randint
nums = [randint(1,3) for _ in range(20)]
print(nums)
"""

solution = Solution()
print(solution.minimumDistance(nums))
