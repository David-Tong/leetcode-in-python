class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = max(nums) * L - sum(nums)
        return ans


nums = [2,1,3]
nums = [4,4,5]

solution = Solution()
print(solution.minMoves(nums))
