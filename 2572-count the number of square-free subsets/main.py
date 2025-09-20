class Solution(object):
    def squareFreeSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        M = len(nums)
        N = 30
        from collections import defaultdict

        # helper function, find all primes under 30
        # def eratosthenes
        primes = defaultdict(int)
        isPrime = [True] * (N + 1)

        def eratosthenes(n):
            isPrime[0] = isPrime[1] = False
            idx = 0
            for x in range(2, n + 1):
                if isPrime[x]:
                    primes[x] = idx
                    idx += 1
                    if x * x > n:
                        continue
                    for y in range(x * x, n + 1, x):
                        isPrime[y] = False

        eratosthenes(N)

        # helper function
        # prime factorization for all numbers under 30
        dicts = defaultdict(list)

        def primeFactorization(n):
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

        for x in range(1, N):
            if x + 1 in primes:
                dicts[x + 1] = {x + 1: 1}
            else:
                dicts[x + 1] = primeFactorization(x + 1)

        # helper function
        # masking
        def masking(num):
            mask = 0
            for key in dicts[num]:
                if dicts[num][key] > 1:
                    return -1
                else:
                    mask += 2 ** primes[key]
            return mask

        masks = defaultdict(int)
        for x in range(0, N):
            masks[x + 1] = masking(x + 1)
        # print(masks)

        # process
        # dp init
        # dp[x][state] - the number of square-free subsets for nums[:x+1] with the state
        # state        - the occurance of prime numbers [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] in the subsets
        L = 2 ** 10
        MODULO = 10 ** 9 + 7
        dp = [[0] * L for _ in range(M)]
        state = masks[nums[0]]
        if state >= 0:
            dp[0][state] = 1

        # dp transfer
        # dp[x][state] = dp[x-1][state] if state & masks[nums[x]] != 0
        # dp[x][new_state] += dp[x-1][state]  if state & masks[nums[x]] == 0
        #                    which means we don't have 2 duplicated prime numbers in the subset
        for x in range(1, M):
            mask = masks[nums[x]]
            if mask >= 0:
                dp[x][mask] += 1

            for state in range(L):
                dp[x][state] = (dp[x][state] + dp[x - 1][state]) % MODULO
                if mask >= 0:
                    if state & mask == 0 and  dp[x - 1][state] > 0:
                        new_state = state | mask
                        dp[x][new_state] = (dp[x][new_state] + dp[x - 1][state]) % MODULO

        # print(dp)
        ans = sum(dp[M - 1]) % MODULO
        return ans


nums = [3,4,4,5]
nums = [1]
nums = [3,2,7,2,7,2,5]

"""
from random import randint
nums = [randint(1, 30) for _ in range(1000)]
print(nums)
"""

nums = [26, 30, 16]

solution = Solution()
print(solution.squareFreeSubsets(nums))
