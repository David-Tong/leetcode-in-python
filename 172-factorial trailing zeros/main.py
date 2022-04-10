class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import log
        upper = int(log(10e4) / log(5))
        ans = 0
        for x in range(1, upper + 1):
            ans += n // pow(5, x)
        return ans


n = 3
n = 5
n = 110

solution = Solution()
print(solution.trailingZeroes(n))
