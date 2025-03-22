class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        idx = L - 1
        left, right = 0 , L - 1

        ans = 0
        while idx >= 0:
            if nums[idx] >= nums[right]:
                left += 1
            else:
                right -= 1
                ans += 1
            idx -= 1
        return ans


nums = [1,3,5,2,1,3,1]
nums = [1,2,3,4]

solution = Solution()
print(solution.maximizeGreatness(nums))
