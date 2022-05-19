class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        def doFind(n, digits):
            base = 10 ** (digits - 1)
            range = 9 * 10 ** (digits - 1) * digits
            if n > range:
                return doFind(n - range, digits + 1)
            else:
                number = base + (int(n) - 1) / digits
                digit = (int(n) - 1) % digits
                return int(str(number)[digit])

        return doFind(n, 1)


n = 3
n = 11

solution = Solution()
print(solution.findNthDigit(n))
