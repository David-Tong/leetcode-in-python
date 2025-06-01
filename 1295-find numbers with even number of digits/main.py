class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        ans = 0
        for num in nums:
            if len(str(num)) %  2 == 0:
                ans += 1
        return ans


nums = [12,345,2,6,7896]
nums = [555,901,482,1771]

solution = Solution()
print(solution.findNumbers(nums))
