class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from math import lcm, gcd
        ans = 0
        for x in range(L):
            pd, lm, gd = nums[x], nums[x], nums[x]
            for y in range(x + 1, L):
                pd, lm, gd = pd * nums[y], lcm(lm, nums[y]), gcd(gd, nums[y])
                if pd == lm * gd:
                    ans = max(ans, y - x + 1)
        return ans


nums = [1,2,1,2,1,1,1]
nums = [2,3,4,5,6]
nums = [1,2,3,1,4,5,1]

solution = Solution()
print(solution.maxLength(nums))
