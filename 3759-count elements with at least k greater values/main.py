class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        from bisect import bisect_right
        ans = 0
        idx = 0
        while idx < L:
            idx2 = bisect_right(nums, nums[idx])
            counts = L - idx2
            if counts >= k:
                ans += 1
            idx += 1
        return ans


nums = [3,1,2]
k = 1

nums = [5,5,5]
k = 2

from random import randint
nums = [randint(1, 10 ** 3) for _ in range(10 ** 5)]
k = 2
print(nums)

solution = Solution()
print(solution.countElements(nums, k))
