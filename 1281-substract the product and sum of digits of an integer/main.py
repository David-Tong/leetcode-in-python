class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = str(n)

        product = 1
        sumi = 0
        for digit in digits:
            product *= int(digit)
            sumi += int(digit)

        return product - sumi


n = 234
n = 4421

solution = Solution()
print(solution.subtractProductAndSum(n))
