class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.ranks[px] > self.ranks[py]:
                self.parents[py] = px
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True

    def merged(self, x, y):
        px, py = self.find(x), self.find(y)
        return px == py


class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        M = len(nums)
        N = max(nums)

        # use eratosthenes method to sieve primes
        primes = []
        isPrime = [True] * (N + 1)

        def eratosthenes(n):
            isPrime[0] = isPrime[1] = False
            for x in range(2, n + 1):
                if isPrime[x]:
                    primes.append(x)
                    if x * x > n:
                        continue
                    for y in range(x * x, n + 1, x):
                        isPrime[y] = False

        eratosthenes(N)
        prime_idxes = {prime: idx for idx, prime in enumerate(primes)}
        P = len(primes)
        # print(primes)
        # print(prime_idxes)
        # print(P)
        import time
        # print("here0 {}".format(time.time()))

        # get prime factorization for nums
        def primeFactorization(n):
            factors = set()
            for prime in primes:
                count = 0
                while n % prime == 0:
                    count += 1
                    n /= prime
                if count > 0:
                    factors.add(prime)
                if n == 1:
                    return factors

        from collections import defaultdict
        dicts = defaultdict(set)
        for num in nums:
            if num not in dicts:
                factors = primeFactorization(num)
                dicts[num] = factors
        # print(dicts)
        # print("here {}".format(time.time()))

        # process
        # build ufs
        ufs = UnionFindSet(P + M)
        for idx, num in enumerate(nums):
            factors = dicts[num]
            idx2 = 0
            for factor in factors:
                idx2 = prime_idxes[factor]
                ufs.union(idx2, P + idx)
        # print("here2 {}".format(time.time()))
        for idx in range(P + M):
            ufs.find(idx)
        # print("here2.1 {}".format(time.time()))

        # sort
        num_pairs = [(num, idx) for idx, num in enumerate(nums)]
        num_pairs = sorted(num_pairs, key=lambda x:x[0])
        # print(num_pairs)
        # print("here3 {}".format(time.time()))

        # check
        for x in range(M):
            idx = P + x
            idx2 = P + num_pairs[x][1]
            if not ufs.merged(idx, idx2):
                return False
        return True


nums = [7,21,3]
nums = [5,2,6,2]
nums = [10,5,9,3,15]

from random import randint
nums = [randint(2, 10 ** 5) for _ in range(3 * 10 ** 4)]
# print(nums)

solution = Solution()
print(solution.gcdSort(nums))
