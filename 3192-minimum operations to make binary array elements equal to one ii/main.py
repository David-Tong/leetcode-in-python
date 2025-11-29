class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        pivot = 1
        ans = 0
        for num in nums:
            if num != pivot:
                ans += 1
                pivot = 1 - pivot
        return ans


nums = [0,1,1,0,1]
nums = [1,0,0,0]

solution = Solution()
print(solution.minOperations(nums))
