class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums = sorted(nums)
        ans = set()
        for x in range(N):
            l = x + 1
            r = N - 1
            while l < r:
                sumi = nums[x] + nums[l] + nums[r]
                if sumi == 0:
                    ans.add((nums[x], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sumi < 0:
                    l += 1
                else:
                    r -= 1
        return ans


nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
print(solution.threeSum(nums))