class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxis = [0] * L
        for x in range(L - 1, -1, -1):
            if x == L - 1:
                maxis[x] = nums[x]
            else:
                maxis[x] = max(maxis[x + 1], nums[x])
        # print(maxis)

        # process
        ans = -1
        for x in range(L - 1):
            if nums[x] < maxis[x + 1]:
                ans = max(ans, maxis[x + 1] - nums[x])
        return ans


nums = [7,1,5,4]
nums = [9,4,3,2]
nums = [1,5,2,10]

solution = Solution()
print(solution.maximumDifference(nums))
