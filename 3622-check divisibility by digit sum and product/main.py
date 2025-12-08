class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # pre-process
        digits = list()
        num = n
        while num:
            digit = num % 10
            digits.append(digit)
            num = num // 10
        total = sum(digits)
        product = 1
        for digit in digits:
            product *= digit

        # process
        return n % (total + product) == 0


n = 99
n = 23


solution = Solution()
print(solution.checkDivisibility(n))
