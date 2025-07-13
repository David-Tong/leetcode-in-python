class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxis, minis = [0] * L, [0] * L
        # find maxi from left to right
        for x in range(L):
            if x == 0:
                maxis[x] = nums[x]
            else:
                maxis[x] = max(maxis[x - 1], nums[x])
        # find mini from right to left
        for x in range(L - 1, -1, -1):
            if x == L - 1:
                minis[x] = nums[x]
            else:
                minis[x] = min(minis[x + 1], nums[x])

        # process
        ans = 0
        for x in range(1, L - 1):
            if maxis[x - 1] < nums[x] < minis[x + 1]:
                ans += 2
            elif nums[x - 1] < nums[x] < nums[x + 1]:
                ans += 1
        return ans


nums = [1,2,3]
nums = [2,4,6,4]
nums = [3,2,1]

solution = Solution()
print(solution.sumOfBeauties(nums))
