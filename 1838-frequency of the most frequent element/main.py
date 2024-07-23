class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L = len(nums)
        nums = sorted(nums)

        prefix = [0] * (L + 1)
        prefix[0] = 0
        for x in range(L):
            prefix[x + 1] = prefix[x] + nums[x]

        def doFrequency(target, nums, prefix, k):
            for x in range(target, L + 1):
                if (nums[x - 1] * target) - (prefix[x] - prefix[x - target]) <= k:
                    return True
            return False

        left = 1
        right = len(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if doFrequency(middle, nums, prefix, k):
                left = middle
            else:
                right = middle - 1

        if doFrequency(right, nums, prefix, k):
            return right
        else:
            return left