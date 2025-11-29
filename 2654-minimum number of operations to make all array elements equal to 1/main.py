class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        # gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # short-cut
        # conner case 1 : one exists
        ones = 0
        for x in range(L):
            if nums[x] == 1:
                ones += 1
        if ones > 0:
            return L - ones

        # conner case 2 : gcds not equal to 1
        gcds = nums[0]
        for x in range(1, L):
            gcds = gcd(gcds, nums[x])
        if gcds != 1:
            return -1

        # process
        mini = float("inf")
        for x in range(L):
            gcds = nums[x]
            for y in range(x + 1, L):
                gcds = gcd(gcds, nums[y])
                if gcds == 1:
                    mini = min(mini, y - x + 1)
                    break
        ans = L - 1 + (mini - 1)
        return ans


nums = [2,6,3,4]
nums = [2,10,6,14]

"""
from random import randint
nums = [randint(1, 10 ** 6) for _ in range(50)]
print(nums)
"""

nums = [6,10,15]

solution = Solution()
print(solution.minOperations(nums))
