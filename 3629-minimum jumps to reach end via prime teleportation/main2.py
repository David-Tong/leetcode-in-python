class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        N = len(nums)
        M = max(nums)

        # short-cut
        if N == 1:
            return 0

        # reversed index
        from collections import defaultdict
        dicts = defaultdict(set)
        for idx, num in enumerate(nums):
            dicts[num].add(idx)

        # sieve primes
        primes = defaultdict(set)
        isPrime = [True] * (M + 1)
        def eratosthenes(m):
            isPrime[0] = isPrime[1] = False
            for x in range(2, m + 1):
                primes[x] = set()
                if isPrime[x]:
                    if x * x > m:
                        continue
                    for y in range(x * x, m + 1, x):
                        isPrime[y] = False

        eratosthenes(M)
        # print(isPrime)

        # factorize
        def primeFactorization(num):
            target = num
            for prime in primes.keys():
                while target % prime == 0:
                    target //= prime
                    primes[prime].add(num)
                if target == 1:
                    return

        for num in set(nums):
            primeFactorization(num)

        # print(primes)

        # process
        from collections import deque
        bfs = deque()
        bfs.append(0)
        visited = [False] * N
        visited[0] = True

        step = 1
        while bfs:
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                if curr < N - 1:
                    nxt = curr + 1
                    if nxt == N - 1:
                        return step
                    if not visited[nxt]:
                        bfs.append(nxt)
                        visited[nxt] = True

                if curr > 0:
                    nxt = curr - 1
                    if not visited[nxt]:
                        bfs.append(nxt)
                        visited[nxt] = True

                if isPrime[nums[curr]]:
                    prime = nums[curr]
                    if nums[N - 1] % prime == 0:
                        return step
                    teleportations = primes[prime]
                    for teleportation in teleportations:
                        for nxt in dicts[teleportation]:
                            if not visited[nxt]:
                                bfs.append(nxt)
                                visited[nxt] = True
            step += 1
        return step


nums = [1,2,4,6]
nums = [2,3,4,7,9]
nums = [4,6,5,8]
nums = [1,1,1,1]
nums = [2,2,2,2]

nums = [1,3,6,6,6,6,6,6,6,6,6,2,10]

from random import randint
nums = [randint(1, 10 ** 6) for _ in range(10 ** 5)]
print(nums)

solution = Solution()
print(solution.minJumps(nums))
