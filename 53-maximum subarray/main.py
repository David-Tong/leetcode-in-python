class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        res = [0] * length
        if length == 0:
            return 0
        for i in range(length):
            if i == 0:
                res[i] = nums[i]
            else:
                res[i] = max(nums[i], res[i-1] + nums[i])
        return max(res)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
solution = Solution()
print(solution.maxSubArray(nums2))