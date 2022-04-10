class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums = sorted(nums)

        ans = 0
        mini = float("inf")
        for x in range(N):
            l = x + 1
            r = N - 1
            while l < r:
                sumi = nums[l] + nums[r] + nums[x]
                if sumi == target:
                    return sumi
                elif sumi < target:
                    l += 1
                else:
                    r -= 1
                if abs(sumi - target) < mini:
                    mini = abs(sumi - target)
                    ans = sumi
        return ans


nums = [-1, 2, 1, -4]
target = 1

nums = [0, 0, 0]
target = 1

nums = [0, 1, 2]
target = 3

solution = Solution()
print(solution.threeSumClosest(nums, target))
