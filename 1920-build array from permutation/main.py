class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        # process
        ans = [0] * L
        for x in range(L):
            ans[x] = nums[nums[x]]
        return ans


nums = [0,2,1,5,3,4]
nums = [5,0,1,2,3,4]

solution = Solution()
print(solution.buildArray(nums))
