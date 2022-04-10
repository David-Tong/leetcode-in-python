class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        from math import sqrt
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        for x in range(2, int(sqrt(n)) + 1):
            if primes[x] == 1:
                primes[x*x:n:x] = [0] * len(primes[x*x:n:x])
        return sum(primes)


n = 10
n = 0
n = 629238
n = 417498

solution = Solution()
print(solution.countPrimes(n))