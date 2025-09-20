class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        maxi = max(nums)
        nums = sorted(nums)
        L = len(nums)

        # process
        if L < maxi + 1:
            return False

        for x in range(L - 1):
            if nums[x] != x + 1:
                return False

        if nums[L - 1] != maxi:
            return False

        return True


nums = [2, 1, 3]
nums = [1, 3, 3, 2]
nums = [1, 1]
nums = [3, 4, 4, 1, 2, 1]
nums = [1, 2, 3, 4, 3]
nums = [2, 3, 4, 3]

solution = Solution()
print(solution.isGood(nums))
