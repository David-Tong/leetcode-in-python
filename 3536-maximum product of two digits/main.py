class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        digits = list()
        for digit in str(n):
            digits.append(int(digit))
        digits = sorted(digits, reverse=True)

        # process
        ans = digits[0] * digits[1]
        return ans


n = 31
n = 22
n = 124

solution = Solution()
print(solution.maxProduct(n))
