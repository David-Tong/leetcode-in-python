class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        ans = 0
        for x in range(L):
            maxi = float("-inf")
            mini = float("inf")
            for y in range(x, L):
                maxi = max(maxi, nums[y])
                mini = min(mini, nums[y])
                ans += maxi - mini
        return ans


nums = [1,2,3]
nums = [1,3,3]
nums = [4,-2,-3,4,1]

solution = Solution()
print(solution.subArrayRanges(nums))
