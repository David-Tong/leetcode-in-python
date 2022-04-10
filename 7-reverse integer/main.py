class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(x)
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -1 * int(str(-1 * x)[::-1])

        if x > 2**31 - 1 or x < -1 * 2**31:
            return 0
        else:
            return x


x = 123
x = -123
x = 120
x = 1534236469

solution = Solution()
print(solution.reverse(x))
