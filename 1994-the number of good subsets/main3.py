class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        M = 30

        # find primes under 30
        from collections import defaultdict
        primes = []
        isPrime = [True] * (M + 1)

        def eratosthenes(n):
            isPrime[0] = isPrime[1] = False
            for x in range(2, n + 1):
                if isPrime[x]:
                    primes.append(x)
                    if x * x > n:
                        continue
                    for y in range(x * x, n + 1, x):
                        isPrime[y] = False

        eratosthenes(M)
        # print(primes)

        # do prime factorization for 1 to 30
        def primeFactorization(n):
            from collections import defaultdict
            factors = defaultdict(int)
            for prime in primes:
                count = 0
                while n % prime == 0:
                    count += 1
                    n /= prime
                if count == 1:
                    factors[prime] = count
                elif count > 1:
                    return None
                if n == 1:
                    return factors

        primes_factors = defaultdict(dict)
        for x in range(1, M):
            factors = primeFactorization(x + 1)
            if factors:
                primes_factors[x + 1] = factors
        # print(primes_factors)

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        # print(counts)

        # get all valid subsets
        L = 2 ** len(primes_factors)
        candidates = sorted(primes_factors.keys())
        subsets = list()
        for mask in range(1, L):
            target = mask
            idx = 0
            subset = set()
            factors = defaultdict()
            while target:
                if target & 1:
                    subset.add(candidates[idx])
                    for factor in primes_factors[candidates[idx]]:
                        if factor not in factors:
                            factors[factor] = 0
                        factors[factor] += primes_factors[candidates[idx]][factor]
                idx += 1
                target >>= 1
            valid = True
            for factor in factors:
                if factors[factor] > 1:
                    valid = False
            if valid:
                subsets.append(subset)
        # print(subsets)

        # process
        # helper function
        MODULO = 10 ** 9 + 7
        from math import factorial
        self.cache = defaultdict()
        def __factorial__(n):
            if n in self.cache:
                return self.cache[n]
            self.cache[n] = factorial(n)
            return self.cache[n]

        def combination(n, k):
            return __factorial__(n) / (__factorial__(n - k) * (__factorial__(k)))

        ones = 0
        print(counts[1])
        for x in range(counts[1] + 1):
            ones = (ones + combination(counts[1], x)) % MODULO
        # print(ones)

        combs = 0
        for subset in subsets:
            comb = 1
            for num in subset:
                comb *= counts[num]
            combs = (combs + comb) % MODULO
        # print(combs)

        ans = (ones * combs) % MODULO
        return ans


nums = [1,2,3,4]
nums = [1,2,2,3,4]
nums = [1,1,2,3,4]
nums = [4,2,3,15]

from random import randint
nums = [randint(1, 30) for _ in range(10 ** 5)]
# print(nums)

nums = [5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]

solution = Solution()
print(solution.numberOfGoodSubsets(nums))
