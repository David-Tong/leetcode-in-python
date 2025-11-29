class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        ans = 0
        for num in nums:
            if num % 3 != 0:
                ans += 1
        return ans


nums = [1,2,3,4]
nums = [3,6,9]

solution = Solution()
print(solution.minimumOperations(nums))
