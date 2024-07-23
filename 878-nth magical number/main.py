class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        from fractions import gcd
        print(gcd(a, b))


n = 1
a = 2
b = 3

n = 1
a = 3
b = 6

n = 1
a = 4
b = 6

solution = Solution()
print(solution.nthMagicalNumber(n, a, b))
