class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        left, right = 0, L - 1
        ans = float("inf")
        while left < right:
            ans = min(ans, (nums[left] + nums[right]) * 1.0 / 2)
            left += 1
            right -= 1
        return ans


nums = [7,8,3,4,15,13,4,1]
nums = [1,9,8,3,10,5]
nums = [1,2,3,7,8,9]

solution = Solution()
print(solution.minimumAverage(nums))
