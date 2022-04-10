class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negatives = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negatives += 1

        if negatives % 2 == 1:
            return -1
        else:
            return 1


nums = [-1, -2, -3, -4, 3, 2, 1]
nums = [1, 5, 0, 2, -3]
#nums = [-1, 1, -1, 1, -1]

solution = Solution()
print(solution.arraySign(nums))
