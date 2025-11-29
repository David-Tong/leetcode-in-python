class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        # pre-process
        # helper function
        # get digit sum
        def digit_sum(x):
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res

        # process
        ds = digit_sum(x)
        return ds if x % ds == 0 else -1


x = 18
x = 23

solution = Solution()
print(solution.sumOfTheDigitsOfHarshadNumber(x))
