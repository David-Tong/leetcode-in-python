class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        ans = [0] * L
        idx = 0
        while idx < L:
            target = (idx + nums[idx] + L) % L
            ans[idx] = nums[target]
            idx += 1
        return ans


nums = [3,-2,1,1]
nums = [-1,4,-1]

solution = Solution()
print(solution.constructTransformedArray(nums))
