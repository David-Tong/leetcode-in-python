class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # help function
        def count(x):
            return x * (x + 1) // 2

        # process
        ans = 0
        c = 1
        for x in range(1, L):
            if nums[x] == nums[x - 1]:
                ans += count(c)
                c = 1
            else:
                c += 1
        ans += count(c)
        return ans


nums = [0,1,1,1]
nums = [1,0,1,0]

from random import randint
nums = [randint(0, 1) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.countAlternatingSubarrays(nums))
