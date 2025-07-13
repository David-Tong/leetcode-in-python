class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        from bisect import bisect_right
        ans = 0
        prev = None
        for x in range(L):
            num = nums[x]
            if prev and prev == num:
                pass
            else:
                idx = bisect_right(nums, num + 1)
                if nums[idx - 1] == num + 1:
                    ans = max(ans, idx - x)
            prev = num
        return ans


nums = [1,3,2,2,5,2,3,7]
nums = [1,2,3,4]
nums = [1,1,1,1]

solution = Solution()
print(solution.findLHS(nums))
