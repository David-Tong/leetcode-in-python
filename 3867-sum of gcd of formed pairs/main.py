class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        from collections import defaultdict
        cache = defaultdict(int)

        from fractions import gcd
        gcds = list()
        maxi = float('-inf')
        for num in nums:
            maxi = max(num, maxi)
            key = "{}-{}".format(num, maxi)
            if key not in cache:
                cache[key] = gcd(num, maxi)
            gcds.append(cache[key])

        # process
        gcds = sorted(gcds)

        ans = 0
        idx = 0
        while idx < L // 2:
            key = "{}-{}".format(gcds[idx], gcds[L - 1 - idx])
            if key not in cache:
                cache[key] = gcd(gcds[idx], gcds[L - 1 - idx])
            ans += cache[key]
            idx += 1
        return ans


nums = [2,6,4]
nums = [3,6,2,8]

from random import randint
nums = [randint(1,10 ** 9) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.gcdSum(nums))
