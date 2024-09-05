class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)

        maxi = float("-inf")
        mini = float("inf")

        maxi_idx = -1
        mini_idx = -1

        maxis = [0] * L
        minis = [0] * L

        # setup
        idx = L - 1
        while idx >= 0:
            if maxi < nums[idx]:
                maxi = nums[idx]
                maxi_idx = idx
            maxis[idx] = (maxi, maxi_idx)

            if mini > nums[idx]:
                mini = nums[idx]
                mini_idx = idx
            minis[idx] = (mini, mini_idx)

            idx -= 1

        # search
        idx = 0
        while idx + indexDifference < L:
            if abs(maxis[idx + indexDifference][0] - nums[idx]) >= valueDifference:
                return [idx, maxis[idx + indexDifference][1]]
            if abs(minis[idx + indexDifference][0] - nums[idx]) >= valueDifference:
                return [idx, minis[idx + indexDifference][1]]
            idx += 1

        return [-1, -1]


nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4

nums = [2,1]
indexDifference = 0
valueDifference = 0

nums = [1,2,3]
indexDifference = 2
valueDifference = 4

nums = [3,4,5,6,7,1,2,3,4,5,61,3,4,12,45]
indexDifference = 7
valueDifference = 30

solution = Solution()
print(solution.findIndices(nums, indexDifference, valueDifference))
