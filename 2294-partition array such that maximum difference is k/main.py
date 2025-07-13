class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        nums = sorted(nums)
        L = len(nums)

        # process
        from bisect import bisect_right
        ans = 0
        idx = 0
        while idx < L:
            ans += 1
            idx = bisect_right(nums, nums[idx] + k)
        return ans


nums = [3,6,1,2,5]
k = 2

nums = [1,2,3]
k = 1

nums = [2,2,4,5]
k = 0

solution = Solution()
print(solution.partitionArray(nums, k))
