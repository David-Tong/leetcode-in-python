class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        L = len(nums)

        for x in range(L):
            for y in range(x + indexDifference, L):
                if abs(nums[y] - nums[x]) >= valueDifference:
                    return [x, y]
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
