class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        count = 1
        ans = 1
        for idx in range(1, N):
            if nums[idx] > nums[idx - 1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans


nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1]
nums = [1,3,5,4,7,1,2,3,4,5,6,7,8]

solution = Solution()
print(solution.findLengthOfLCIS(nums))
