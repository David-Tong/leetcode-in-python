class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums * 2


nums = [1,2,1]

solution = Solution()
print(solution.getConcatenation(nums))
