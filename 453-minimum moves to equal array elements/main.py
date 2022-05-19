class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        ans = 0
        for num in nums:
            ans += num - mini
        return ans


nums = [1,2,3]
nums = [1, 1, 1]
nums = [17,25,44,61]

solution = Solution()
print(solution.minMoves(nums))
