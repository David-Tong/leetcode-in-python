class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        def doUnique(n, digits, selected):
            if n == 0:
                self.ans += 1
            else:
                not_leading_zeros = False
                not_zeros = False
                for num in selected:
                    if num != 0:
                        not_zeros = True
                    if num == 0:
                        if not_zeros:
                            not_leading_zeros = True
                # put other numbers
                for idx, digit in enumerate(digits):
                    if digit == 0:
                        if not not_leading_zeros:
                            doUnique(n - 1, digits, selected + [digit])
                    else:
                        doUnique(n - 1, digits[0:idx] + digits[idx+1:], selected + [digit])

        digits = [_ for _ in range(10)]
        doUnique(n, digits, [])
        return self.ans


n = 8

solution = Solution()
print(solution.countNumbersWithUniqueDigits(n))
