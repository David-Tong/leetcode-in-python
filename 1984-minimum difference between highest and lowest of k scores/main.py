class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # shortcut
        if k == 1:
            return 0

        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = float("inf")
        for x in range(L - k + 1):
            ans = min(ans, nums[x + k - 1] - nums[x])
        return ans


nums = [90]
k = 1

nums = [9,4,1,7]
k = 2

solution = Solution()
print(solution.minimumDifference(nums, k))
