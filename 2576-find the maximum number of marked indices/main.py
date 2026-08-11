class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        H = L // 2
        nums = sorted(nums)

        def can(limit):
            from sortedcontainers import SortedList
            sl = SortedList(nums[limit:])
            idx = 0
            while idx < limit:
                target = nums[idx] * 2
                idx_target = sl.bisect_left(target)
                if idx_target < len(sl):
                    sl.pop(idx_target)
                    idx += 1
                else:
                    return False
            return True

        # process
        # binary search
        left = 0
        right = H
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                left = middle
            else:
                right = middle - 1

        if can(right):
            ans = right * 2
        else:
            ans = left * 2
        return ans


nums = [3,5,2,4]
nums = [9,2,5,4]
nums = [7,6,8]

from random import randint
nums = [randint(1,10) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.maxNumOfMarkedIndices(nums))
