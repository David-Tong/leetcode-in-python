class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = 0
        for x in range(0, L ,2):
            ans += nums[x]
        return ans


nums = [1,4,3,2]
nums = [6,2,6,5,1,2]

solution = Solution()
print(solution.arrayPairSum(nums))
