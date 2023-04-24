class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        total = 0
        for idx, num in enumerate(nums):
            total += num
            if total % (idx + 1) == 0:
                ans = max(ans, total // (idx + 1))
            else:
                ans = max(ans, total // (idx + 1) + 1)
        return ans


nums = [3,7,1,6]
nums = [10,1]
nums = [1,10,10,0,0]

solution = Solution()
print(solution.minimizeArrayValue(nums))
