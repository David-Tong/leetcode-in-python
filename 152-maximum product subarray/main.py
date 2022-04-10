class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        mins = [0] * N
        maxs = [0] * N
        mins[0] = nums[0]
        maxs[0] = nums[0]
        for x in range(1, N):
            maxs[x] = max(max(mins[x-1] * nums[x], maxs[x-1] * nums[x]), nums[x])
            mins[x] = min(min(mins[x-1] * nums[x], maxs[x-1] * nums[x]), nums[x])
        return max(maxs)


nums = [2, 3, -2, 4]
nums = [-2, 0, -1]
nums = [2, -5, -2, -4, 3]

solution = Solution()
print(solution.maxProduct(nums))
