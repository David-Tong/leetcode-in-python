class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxi = max(nums)

        # process
        ans = 0
        l = 0
        for x in range(L):
            if nums[x] == maxi:
                if x > 0 and nums[x] == nums[x - 1]:
                    l += 1
                else:
                    ans = max(ans, l)
                    l = 1
        ans = max(ans, l)
        return ans


nums = [1,2,3,3,2,2]
nums = [1,2,3,4]
nums = [1,2,3,4,5,6,7,2,2,1,1,1,2,2,7,7,7,7,7,8,8,8,9]
nums = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]
nums = [311155,201191,311155,311155,311155,311155,311155,311155,311155,311155]

solution = Solution()
print(solution.longestSubarray(nums))
