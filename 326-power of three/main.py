class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        from math import log10
        log3 = log10(n) / log10(3)
        if log3 == int(log3):
            return True
        else:
            return False


n = 27
n = 28
n = 0
n = -11
n = 2e31 - 1
n = 1
n = 2
n = 243

solution = Solution()
print(solution.isPowerOfThree(n))
