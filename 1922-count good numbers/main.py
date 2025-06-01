class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        if n % 2 == 0:
            evens, odds = n // 2, n // 2
        else:
            evens, odds = n // 2 + 1, n // 2

        # helper function
        # doPow
        def doPow(base, exp):
            if exp == 0:
                return 1
            elif exp == 1:
                return base
            else:
                half = doPow(base, exp // 2)
                if exp % 2 == 0:
                    return half * half % MODULO
                else:
                    return half * half * base % MODULO

        # process
        MODULO = 10 ** 9 + 7
        EVENS, PRIMES = 5, 4
        ans = doPow(EVENS, evens) * doPow(PRIMES, odds) % MODULO
        return ans


n = 1
n = 4
n = 50
n = 10 ** 15

solution = Solution()
print(solution.countGoodNumbers(n))
