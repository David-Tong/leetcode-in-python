class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        presum = 0
        mini = 0
        for num in nums:
            presum += num
            mini = min(mini, presum)

        # process
        ans = 1 - mini
        return ans


nums = [-3,2,-3,4,2]
nums = [1,2]
nums = [1,-2,-3]

solution = Solution()
print(solution.minStartValue(nums))
