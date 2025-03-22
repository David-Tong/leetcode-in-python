class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        left, right = min(nums), max(nums)

        # process
        # helper
        def can(target):
            idx = 0
            count = 0
            while idx < L:
                if nums[idx] <= target:
                    idx += 2
                    count += 1
                else:
                    idx += 1
            if count >= k:
                return True

        # binary search
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1
        if can(left):
            return left
        else:
            return right


nums = [2,3,5,9]
k = 2

nums = [2,7,9,3,1]
k = 2

nums = [2]
k = 1

nums = [2,3,5,6,11,2,3,4,11,5,6,7,8,8,9]
k = 5

solution = Solution()
print(solution.minCapability(nums, k))
