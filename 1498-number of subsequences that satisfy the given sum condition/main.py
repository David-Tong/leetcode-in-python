class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MODUL0 = 10 ** 9 + 7
        nums = sorted(nums)

        from bisect import bisect_right
        ans = 0
        for idx, num in enumerate(nums):
            idx_right = bisect_right(nums, target - num)
            if idx_right > idx:
                ans += 2 ** (idx_right - idx - 1)

        return ans % MODUL0


nums = [3,5,6,7]
target = 9

nums = [3,3,6,8]
target = 10

nums = [2,3,3,4,6,7]
target = 12

solution = Solution()
print(solution.numSubseq(nums, target))
