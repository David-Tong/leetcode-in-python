class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # process
        ans = list()
        for x in range(L):
            left = nums[x] * x - presum[x]
            right = (presum[-1] - presum[x + 1]) - nums[x] * (L - x - 1)
            ans.append(left + right)
        return ans


nums = [2,3,5]
nums = [1,4,6,8,10]
nums = [1,2]
nums = [2,2,2,2,2,2,2]

solution = Solution()
print(solution.getSumAbsoluteDifferences(nums))
