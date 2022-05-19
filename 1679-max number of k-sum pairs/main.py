class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                left += 1
                right -= 1
                ans += 1
            elif total < k:
                left += 1
            else:
                right -= 1
        return ans


nums = [1,2,3,4]
k = 5

nums = [3,1,3,4,3]
k = 6

nums = [1]
k = 1

solution = Solution()
print(solution.maxOperations(nums, k))
