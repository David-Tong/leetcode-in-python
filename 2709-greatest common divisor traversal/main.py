class UnionFindSet(object):
    def __init__(self, N):
        self.size = N
        self.parents = [_ for _ in range(N)]
        self.ranks = [0] * N

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False
        else:
            if self.ranks[parent_x] > self.ranks[parent_y]:
                self.parents[parent_y] = parent_x
            elif self.ranks[parent_x] < self.ranks[parent_y]:
                self.parents[parent_x] = parent_y
            else:
                self.parents[parent_y] = parent_x
                self.ranks[parent_x] += 1
            return True


class Solution(object):
    def canTraverseAllPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from math import sqrt

        def eratosthenes(n):
            is_prime = [True] * (n + 1)
            for x in range(2, int(sqrt(n)) + 1):
                if is_prime[x]:
                    for y in range(x * x, n + 1, x):
                        is_prime[y] = False
            return [x for x in range(2, n + 1) if is_prime[x]]

        # pre-process
        maxi = max(nums)
        primes = eratosthenes(maxi)

        N = len(nums)
        M = len(primes)
        ufs = UnionFindSet(M + N)

        from collections import defaultdict
        lookup = defaultdict(int)
        for idx, prime in enumerate(primes):
            lookup[prime] = N + idx

        # process
        for idx, num in enumerate(nums):
            for prime in primes:
                prime_idx = lookup[prime]
                if prime > num:
                    break

                if prime * prime > num:
                    ufs.union(idx, lookup[num])
                    break

                if num % prime == 0:
                    ufs.union(idx, prime_idx)
                    while num % prime == 0:
                        num /= prime

        # ans
        for x in range(1, N):
            if ufs.find(x) != ufs.find(0):
                return False
        return True


nums = [2,3,6]
nums = [3,9,5]
"""
nums = [4,3,12,8]
nums = [21,88,75]
nums = [21,21,35,20]
"""

solution = Solution()
print(solution.canTraverseAllPairs(nums))
