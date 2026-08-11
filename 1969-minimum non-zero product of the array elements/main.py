class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        # process
        MODULO = 10 ** 9 + 7
        BASE = 2 ** p - 2
        EXP = 2 ** (p - 1) - 1
        ans = pow(BASE, EXP, MODULO) * (BASE + 1) % MODULO
        return ans


p = 1
p = 2
p = 3

solutin = Solution()
print(solutin.minNonZeroProduct(p))
