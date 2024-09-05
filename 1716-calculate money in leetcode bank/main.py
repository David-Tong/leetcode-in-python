class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        remainder = n % 7
        quotient = n // 7

        return quotient * max(0, (quotient - 1)) // 2 * 7 \
            + quotient * sum(range(1, 8)) \
            + quotient * remainder \
            + sum(range(1, remainder + 1))


n = 4
n = 10
n = 20

solution = Solution()
print(solution.totalMoney(n))
