class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        nums = sorted(nums)
        ans = nums[-1] - nums[0]
        left = nums[0] + k
        right = nums[-1] - k
        for x in range(N - 1):
            maxi = max(right, nums[x] + k)
            mini = min(left, nums[x + 1] - k)
            ans = min(ans, maxi - mini)
        return ans


nums = [1, 3, 6]
k = 3

solution = Solution()
print(solution.smallestRangeII(nums, k))
