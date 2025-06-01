class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        for x in range(L - 2):
            if (nums[x] + nums[x + 2]) * 2 == nums[x + 1]:
                ans += 1
        return ans


nums = [1,2,1,4,1]
nums = [1,1,1]

solution = Solution()
print(solution.countSubarrays(nums))
