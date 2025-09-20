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
        primes_idxes = {prime : idx for idx, prime in enumerate(primes)}

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

        def convert(factors):
            mask = 0
            for prime in factors:
                mask |= 1 << primes_idxes[prime]
            return mask

        prime_masks = defaultdict(dict)
        for x in range(1, M):
            factors = primeFactorization(x + 1)
            if factors:
                prime_masks[x + 1] = convert(factors)
        candidates = prime_masks.keys()
        C = len(candidates)

        # print(prime_masks)
        # print(candidates)

        # use dp to get all valid candidates combination mask
        from copy import deepcopy
        product_masks = [set() for _ in range(C)]
        candidates_masks = defaultdict(set)

        candidate = candidates[0]
        candidate_prime_mask = prime_masks[candidate]
        product_masks[0].add(candidate_prime_mask)
        candidates_masks[candidate_prime_mask].add(1)

        for x in range(1, C):
            candidate_prime_mask = prime_masks[candidates[x]]
            candidates_masks[candidate_prime_mask].add(1 << x)
            product_masks[x].add(candidate_prime_mask)
            for product_mask in product_masks[x - 1]:
                product_masks[x].add(product_mask)
                if product_mask & candidate_prime_mask == 0:
                    new_product_mask = product_mask | candidate_prime_mask
                    product_masks[x].add(new_product_mask)
                    candidate_masks_for_product_mask = deepcopy(candidates_masks[product_mask])
                    for candidate_masks in candidate_masks_for_product_mask:
                        candidates_masks[new_product_mask].add(candidate_masks | 1 << x)

        # print(candidates_masks.keys())
        # print(candidates_masks)

        # count
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        # print(counts)

        # process
        # helper function
        MODULO = 10 ** 9 + 7

        def quickPow(num, n):
            if n == 0:
                return 1
            elif n % 2 == 1:
                return quickPow(num, n - 1) * num % MODULO
            else:
                temp = quickPow(num, n // 2)
                return temp * temp % MODULO

        ones = quickPow(2, counts[1]) % MODULO

        combinations = 0
        for product_mask in candidates_masks:
            for candidate_mask in candidates_masks[product_mask]:
                combination = 1
                target = candidate_mask
                idx = 0
                while target:
                    if target & 1:
                        candidate = candidates[idx]
                        combination *= counts[candidate]
                    target >>= 1
                    idx += 1
                combinations = (combinations + combination) % MODULO
        # print(combinations)

        ans = (ones * combinations) % MODULO
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