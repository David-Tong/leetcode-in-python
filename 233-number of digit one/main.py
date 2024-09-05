class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = 10

        # pre-process
        ones = list()
        ones.append(0)
        for x in range(1, N):
            ones.append(ones[-1] * 10 + 10 ** (x - 1))

        def count(number):
            # handle leading zeros
            number = str(long(number))
            L = len(number)

            # end condition
            if L == 1:
                if int(number) >= 1:
                    return 1
                else:
                    return 0

            print(number)
            if number[0] == "1":
                return ones[L - 1] + long(number[1:]) + 1 + count(number[1:])
            else:
                return ones[L - 1] * int(number[0]) + 10 ** (L - 1) + count(number[1:])

        return count(str(n))


n = 13
n = 0
n = 2893
n = 1730
n = 1
n = 100
n = 101
n = 1001
n = 1000000000

solution = Solution()
print(solution.countDigitOne(n))
