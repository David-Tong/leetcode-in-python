class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        left = 0
        right = 0
        span = 0

        ans = 0
        while right < L:
            span += nums[right]
            while span < right - left:
                span -= nums[left]
                left += 1
            ans = max(ans, right - left)
            right += 1
        return ans


nums = [1,1,0,1]
nums = [0,1,1,1,0,1,1,0,1]
nums = [1,1,1]
nums = [1]
nums = [0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0]

solution = Solution()
print(solution.longestSubarray(nums))
