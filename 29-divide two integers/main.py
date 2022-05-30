class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = False
        if dividend * divisor < 0:
            negative = True

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor << shift:
                shift += 1
            res += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)

        if negative:
            res = -1 * res

        MAX_VALUE = 2 ** 31 - 1
        MIN_VALUE = 2 ** 31 * -1

        if res > MAX_VALUE:
            return MAX_VALUE
        elif res < MIN_VALUE:
            return MIN_VALUE
        else:
            return res


dividend = 10
divisor = 3

dividend = 7
divisor = -3

solution = Solution()
print(solution.divide(dividend, divisor))
