class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        idx = 0
        while idx < L:
            if nums[idx] < 0:
                nums[idx] *= -1
            idx += 1
        nums = sorted(nums)

        # process
        from bisect import bisect_right
        ans = 0
        idx = 0
        while idx < len(nums):
            target = nums[idx] * 2
            idx2 = bisect_right(nums, target)
            if idx2 < L:
                if nums[idx2] == target:
                    ans += idx2 - idx
                else:
                    ans += idx2 - idx - 1
            else:
                ans += idx2 - idx - 1
            idx += 1
        return ans


nums = [0,1,2,3]
nums = [-3,2,-1,4]
nums = [1,10,100,1000]

from random import randint
nums = [randint(-10 ** 5, 10 ** 5) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.perfectPairs(nums))
