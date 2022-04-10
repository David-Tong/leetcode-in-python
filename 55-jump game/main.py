class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        limit = 0
        for idx, num in enumerate(nums):
            if idx <= limit:
                limit = max(limit, idx + num)
            else:
                return False
        return True


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
nums = [0]

solution = Solution()
print(solution.canJump(nums))
