class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        nums = sorted(nums)

        # process
        left = 0
        right = L - 1

        ans = 0
        while left < right:
            ans = max(ans, nums[left] + nums[right])
            left += 1
            right -= 1
        return ans


nums = [3,5,2,3]
nums = [3,5,4,2,4,6]
nums = [1,1]

solution = Solution()
print(solution.minPairSum(nums))
