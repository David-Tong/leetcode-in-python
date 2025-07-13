class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # conner case
        if num == 1:
            return False

        # pre-process
        from math import sqrt
        end = int(sqrt(num))
        factors = list()
        for x in range(1, end + 1):
            if num % x == 0:
                factors.append(x)
                if x != 1:
                    factors.append(num // x)

        # process
        return sum(factors) == num


num = 28
num = 7
num = 2
num = 3
num = 100000000
num = 1

solution = Solution()
print(solution.checkPerfectNumber(num))
