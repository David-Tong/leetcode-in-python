class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxi = max(nums)

        primes = []
        isPrime = [True] * (maxi + 1)

        def eratosthenes(n):
            isPrime[0] = isPrime[1] = False
            for x in range(2, n + 1):
                if isPrime[x]:
                    primes.append(x)
                    if x * x > n:
                        continue
                    for y in range(x * x, n + 1, x):
                        isPrime[y] = False

        eratosthenes(maxi)

        # process
        left, right = -1, -1
        idx = 0
        while idx < L:
            num = nums[idx]
            if isPrime[num]:
                left = idx
                break
            idx += 1

        idx = L - 1
        while idx >= 0:
            num = nums[idx]
            if isPrime[num]:
                right = idx
                break
            idx -= 1

        ans = right - left
        return ans


nums = [4,2,9,5,3]
nums = [4,8,2,8]

solution = Solution()
print(solution.maximumPrimeDifference(nums))
