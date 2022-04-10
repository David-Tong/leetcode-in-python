class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans


nums = [2, 2, 1]
nums = [4, 1, 2, 1, 2]
nums = [4, 1, -2, 1, -2]
#nums = [1]

solution = Solution()
print(solution.singleNumber(nums))
