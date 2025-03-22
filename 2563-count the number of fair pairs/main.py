from stringold import rindex


class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        from bisect import bisect_left, bisect_right
        ans = 0
        for idx, num in enumerate(nums):
            left = lower - num
            idx_left = bisect_left(nums, left, idx + 1)
            right = upper - num
            idx_right = bisect_right(nums, right, idx + 1)
            ans += idx_right - idx_left
        return ans


nums = [0,1,7,4,4,5]
lower = 3
upper = 6

nums = [1,7,9,2,5]
lower = 11
upper = 11

nums = [1,2,3,4,4,4,5,5,5,7,8,9]
lower = 5
upper = 15

"""
nums = [1]
lower = 0
upper = 2
"""

solution = Solution()
print(solution.countFairPairs(nums, lower, upper))

