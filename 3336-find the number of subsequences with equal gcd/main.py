class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        MODULO = 10 ** 9 + 7

        # process
        from collections import defaultdict
        cache = defaultdict(int)

        # dfs
        # return the number of pair count when nums[:x+1]
        #   and with gcd value y for subsequence 1 and
        #   gcd value z for subsequence 2
        from fractions import gcd
        def dfs(x, y, z):
            key = "{}-{}-{}".format(x, y, z)
            if key in cache:
                return cache[key]
            if x < 0:
                res = 1 if y == z else 0
            else:
                res = (dfs(x - 1, y, z) + dfs(x - 1, gcd(y, nums[x]), z) + dfs(x - 1, y, gcd(z, nums[x]))) % MODULO
            cache[key] = res
            return res

        # main
        ans = (dfs(L - 1, 0, 0) - 1) % MODULO
        return ans


nums = [1,2,3,4]
nums = [10,20,30]
nums = [1,1,1,1]
nums = [2,2]

from random import randint
nums = [randint(1,200) for _ in range(200)]
print(nums)

solution = Solution()
print(solution.subsequencePairCount(nums))
