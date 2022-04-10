class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros = 0
        left = 0
        right = 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            right += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left)
        return ans


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

nums = [0]
k = 0

solution = Solution()
print(solution.longestOnes(nums, k))
