class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # pre-process
        digits = list()
        for digit in str(num):
            digits.append(int(digit))
        digits = sorted(digits)

        # process
        ans = digits[0] * 10 + digits[1] * 10 + digits[2] + digits[3]
        return ans


num = 2932
num = 4009

solution = Solution()
print(solution.minimumSum(num))
