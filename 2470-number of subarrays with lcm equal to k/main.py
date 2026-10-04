class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from math import lcm
        ans = 0
        for x in range(L):
            target = 1
            for y in range(x, L):
                target = lcm(target, nums[y])
                if target == k:
                    ans += 1
        return ans


nums = [3,6,2,7,1]
k = 6

nums = [3]
k = 2

nums = [2,2,4]
k = 4

solution = Solution()
print(solution.subarrayLCM(nums, k))