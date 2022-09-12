class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        nums = sorted(nums)
        for x in range(L + 1):
            from bisect import bisect_left
            idx = bisect_left(nums, x)
            if x == L - idx:
                return x
        return -1


nums = [3,5]
nums = [0,0]
nums = [0,4,3,0,4]

solution = Solution()
print(solution.specialArray(nums))
