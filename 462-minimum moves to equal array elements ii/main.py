class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L % 2 == 1:
            median_idx = L // 2
        else:
            median_idx = L // 2 - 1

        nums = sorted(nums)
        median = nums[median_idx]
        ans = 0
        for num in nums:
            ans += abs(num - median)
        return ans


nums = [1,2,3]
nums = [1,10,2,9]
nums = [1,0,0,8,6]

solution = Solution()
print(solution.minMoves2(nums))
