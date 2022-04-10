class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        # save max and min subarray sum
        mins = [0] * N
        maxs = [0] * N
        mins[0] = nums[0]
        maxs[0] = nums[0]
        for x in range(1, N):
            maxs[x] = max(0, maxs[x-1]) + nums[x]
            mins[x] = min(0, mins[x-1]) + nums[x]

        maxi = max(maxs)
        mini = min(mins)

        sumi = sum(nums)
        if mini == sumi:
            return maxi
        else:
            return max(maxi, sumi - mini)


nums = [1, -2, 3, -2]
nums = [5, -3, 5]
nums = [-3, -2, -3]
nums = [-10, -7, 9, -7, 6, 9, -9, -4, -8, -5]

solution = Solution()
print(solution.maxSubarraySumCircular(nums))
