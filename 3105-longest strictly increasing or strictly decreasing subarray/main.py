class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        # search longest strictly increasing subarray
        ans = 0
        longest = 1
        for x in range(L - 1):
            if nums[x] < nums[x + 1]:
                longest += 1
            else:
                ans = max(ans, longest)
                longest = 1
        ans = max(ans, longest)

        # search longest strictly decreasing subarray
        longest = 1
        for x in range(L - 1):
            if nums[x] > nums[x + 1]:
                longest += 1
            else:
                ans = max(ans, longest)
                longest = 1
        ans = max(ans, longest)

        return ans


nums = [1,4,3,3,2]
nums = [3,3,3,3]
nums = [3,2,1]
nums = [1,1,5]

solution = Solution()
print(solution.longestMonotonicSubarray(nums))
