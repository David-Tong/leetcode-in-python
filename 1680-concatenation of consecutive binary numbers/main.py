class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        total = ""
        for x in range(n):
            total = total + bin(x + 1)[2:]
        return int(total, 2) % MODULO


n = 12

solution = Solution()
print(solution.concatenatedBinary(n))
