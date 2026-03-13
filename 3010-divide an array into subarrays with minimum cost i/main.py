class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        ans = sum(sorted(nums[1:])[:2]) + nums[0]
        return ans


nums = [1,2,3,12]

solution = Solution()
print(solution.minimumCost(nums))
