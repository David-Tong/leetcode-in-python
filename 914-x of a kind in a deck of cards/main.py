class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for d in deck:
            dicts[d] += 1

        mini = min(dicts.values())

        # helper function
        primes = []
        isPrime = [True] * (mini + 1)

        def eratosthenes(n):
            isPrime[0] = isPrime[1] = False
            for x in range(2, n + 1):
                if isPrime[x]:
                    primes.append(x)
                    if x * x > n:
                        continue
                    for y in range(x * x, n + 1, x):
                        isPrime[y] = False
        eratosthenes(mini)

        def primeFactorization(n):
            from collections import defaultdict
            factors = defaultdict(int)
            for prime in primes:
                count = 0
                while n % prime == 0:
                    count += 1
                    n /= prime
                if count > 0:
                    factors[prime] = count
                if n == 1:
                    return factors

        factors = primeFactorization(mini)
        # print(factors)

        # process
        if mini == 1:
            return False
        else:
            for factor in factors:
                divisible = True
                for key in dicts:
                    if dicts[key] % factor != 0:
                        divisible = False
                if divisible:
                    return True
        return False


deck = [1,2,3,4,4,3,2,1]
deck = [1,1,1,2,2,2,3,3]
deck = [1,1,1,1,2,2,2,2,2,2]
deck = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]

solution = Solution()
print(solution.hasGroupsSizeX(deck))
