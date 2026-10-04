class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans =0
        idx = 0
        while idx < L:
            if idx % 2 == 0:
                ans += nums[idx]
            else:
                ans -= nums[idx]
            idx += 1
        return ans


nums = [1,3,5,7]
nums = [100]

solution = Solution()
print(solution.alternatingSum(nums))
