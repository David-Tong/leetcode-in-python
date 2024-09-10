class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [_ for _ in nums if _ != 0]
        L = len(nums)

        if L < 3:
            return 0

        nums = sorted(nums)

        from bisect import bisect_left
        ans = 0
        for x in range(L):
            for y in range(x + 1, L):
                total = nums[x] + nums[y]
                idx = bisect_left(nums, total)
                ans += idx - y - 1
        return ans


nums = [2,2,3,4]
nums = [4,2,3,4]
nums = [2,2,2,4]
nums = [0,0,0]
nums = [0,0]
nums = [0,0,2]

solution = Solution()
print(solution.triangleNumber(nums))
