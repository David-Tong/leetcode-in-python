class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_VALUE = 0x7FFFFFFF
        MIN_VALUE = 0x80000000
        MASK = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & MASK, (a & b) << 1 & MASK
        return a if a < MAX_VALUE else ~(a ^ MASK)


a = 1
b = 2

a = 2
b = 3

a = -1000
b = 1000

a = -1000
b = 0

a = -2
b = -8

solution = Solution()
print(solution.getSum(a, b))
