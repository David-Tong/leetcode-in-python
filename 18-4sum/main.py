class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums = sorted(nums)
        ans = set()
        for x in range(N):
            for y in range(x + 1, N):
                l = y + 1
                r = N - 1
                while l < r:
                    sumi = nums[x] + nums[y] + nums[l] + nums[r]
                    if sumi < target:
                        l += 1
                    elif sumi > target:
                        r -= 1
                    else:
                        ans.add((nums[x], nums[y], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0

solution = Solution()
print(solution.fourSum(nums, target))
