class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # count function
        def hasMoreThanKPair(target):
            from bisect import bisect_right
            count = 0
            for x in range(L):
                idx = bisect_right(nums, nums[x] + target)
                count += idx -1 - x

            if count >= k:
                return True
            else:
                return False

        # binary search
        left = 0
        right = 10 ** 6

        while left + 1 < right:
            middle = (left + right) // 2
            if hasMoreThanKPair(middle):
                right = middle
            else:
                left = middle + 1

        if hasMoreThanKPair(left):
            return left
        else:
            return right


nums = [1,3,1]
k = 1

nums = [1,1,1]
k = 2

nums = [1,6,1]
k = 3

nums = [1,2,3,4,4,6,7]
k = 5

nums = [1,2,3,4,4,6,7]
k = 10

solution = Solution()
print(solution.smallestDistancePair(nums, k))
