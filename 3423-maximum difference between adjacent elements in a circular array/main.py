class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        for x in range(1, L):
            ans = max(ans, abs(nums[x] - nums[x - 1]))
        ans = max(ans, abs(nums[L - 1] - nums[0]))
        return ans


nums = [1,2,4]
nums = [-5,-10,-5]
nums = [1,2,10]

solution = Solution()
print(solution.maxAdjacentDistance(nums))
