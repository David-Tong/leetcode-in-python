class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        isPrime = [True] * (L + 1)
        def eratosthenes(L):
            isPrime[0] = isPrime[1] = False
            for x in range(2, L + 1):
                if isPrime[x]:
                    if x * x > L:
                        continue
                    for y in range(x * x, L + 1, x):
                        isPrime[y] = False

        eratosthenes(L)
        print(isPrime)

        # process
        idx = 0
        prime_total = 0
        other_total = 0
        while idx < L:
            if isPrime[idx]:
                prime_total += nums[idx]
            else:
                other_total += nums[idx]
            idx += 1
        ans = abs(prime_total - other_total)
        return ans


nums = [2,3,4]
nums = [-1,5,7,0]

solution = Solution()
print(solution.splitArray(nums))
