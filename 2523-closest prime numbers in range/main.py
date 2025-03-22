from bisect import bisect


class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # pre-process
        primes = []
        isPrime = [False] * (right + 1)

        # eratosthenes algorithm
        isPrime[0] = isPrime[1] = False
        for x in range(2, right + 1):
            isPrime[x] = True
        for x in range(2, right + 1):
            if isPrime[x]:
                primes.append(x)
                if x * x > right:
                    continue
                for y in range(x * x, right + 1, x):
                    isPrime[y] = False
        # print(primes)

        # process
        from bisect import bisect_left
        idx = bisect_left(primes, left)
        mini = float("inf")
        ans = [-1, -1]
        L = len(primes)
        while idx + 1 < L:
            if primes[idx + 1] - primes[idx] < mini:
                mini = primes[idx + 1] - primes[idx]
                ans = [primes[idx], primes[idx + 1]]
            idx += 1
        return ans

left = 10
right = 19

left = 4
right = 6

solution = Solution()
print(solution.closestPrimes(left, right))
