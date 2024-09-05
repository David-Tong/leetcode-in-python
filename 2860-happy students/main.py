class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        nums = sorted(nums)
        ans = 0

        for x in range(L - 1):
            # case 1: strictly greater than nums[x] if selected
            # case 2: strictly less than nums[x] if not selected
            if x + 1 > nums[x] and x + 1 < nums[x + 1]:
                ans += 1

        # corner cases
        if nums[0] > 0:
            ans += 1
        if nums[-1] < L:
            ans += 1

        return ans


nums = [1,1]
nums = [6,0,3,3,6,7,2,7]
nums = [1,2,3,4,5,6,3,2,9,11,2]

solution = Solution()
print(solution.countWays(nums))
