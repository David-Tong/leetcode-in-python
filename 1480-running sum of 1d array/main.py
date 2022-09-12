class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        prefixes = [0] * N

        prefixes[0] = nums[0]
        for x in range(1, N):
            prefixes[x] += prefixes[x-1] + nums[x]

        return prefixes


nums = [1,2,3,4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
nums = [1]

solution = Solution()
print(solution.runningSum(nums))
