class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        nums = list(set(nums))
        L = len(nums)
        print(nums)
        digits = [bin(num).count("1") for num in nums]
        digits = sorted(digits)
        print(digits)

        # process
        from bisect import bisect_left
        ans = 0
        for x in range(L):
            target = k - digits[x]
            idx = bisect_left(digits, target)
            ans += L - idx
        return ans

nums = [1,2,3,1]
k = 3

nums = [5,1,1]
k = 10

nums = [2,7,6,10,4,9,3,7,9,10]
k = 3

nums = [2,3,4,6]
k = 3

from random import randint
nums = [randint(1, 10 ** 9) for _ in range(5000)]
k = 3
print(nums)

solution = Solution()
print(solution.countExcellentPairs(nums, k))
