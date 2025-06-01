from itertools import count

from numpy.ma import floor


class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        # pre-process
        # helper functions
        # eratosthenes sieve method
        def eratosthenes(v):
            primes = list()
            is_primes = [True] * (v + 1)
            is_primes[0] = is_primes[1] = False
            for x in range(2, v + 1):
                if is_primes[x]:
                    primes.append(x)
                    if x * x > v:
                        continue
                    for y in range(x * x, v + 1, x):
                        is_primes[y] = False
            return primes

        # prime factorization
        def primeFactorization(v, primes):
            from collections import defaultdict
            factors = defaultdict(int)
            for prime in primes:
                count = 0
                while v % prime == 0:
                    count += 1
                    v /= prime
                if count > 0:
                    factors[prime] = count
                if v == 1:
                    return factors

        primes = eratosthenes(maxValue)

        # dp[x][y] - the count to place y same factors in x places,
        # allowing multiple factors in the same place
        MODULO = 10 ** 9 + 7
        from math import log
        M = n
        N = int(log(maxValue, 2)) + 1
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = 1
        for x in range(1, M + 1):
            dp[x][0] = 1
            for y in range(1, N + 1):
                for z in range(y + 1):
                    dp[x][y] = (dp[x][y] + dp[x - 1][y - z]) % MODULO
        # print(dp)

        # process
        ans = 0
        for x in range(1, maxValue + 1):
            prime_factors = primeFactorization(x, primes)
            counts = 1
            if prime_factors:
                for factor in prime_factors:
                    counts = counts * dp[n][prime_factors[factor]] % MODULO
            ans = (ans + counts) % MODULO
        return ans


n = 2
maxValue = 5

n = 5
maxValue = 3

n = 3
maxValue = 30

n = 10
maxValue = 1

n = 10000
maxValue = 10000

n = 2
maxValue = 1

solution = Solution()
print(solution.idealArrays(n, maxValue))
