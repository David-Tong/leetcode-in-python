class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        # get all primes less than and equal to 1000
        from math import sqrt
        L = 1000
        primes = list()
        for num in range(2, L):
            primize = True
            for x in range(2, int(sqrt(num)) + 1):
                if num % x == 0:
                    primize = False
                    break
            if primize:
                primes.append(num)
        primes = [0] + primes
        print(primes)

        # process
        previous = 0
        from bisect import bisect_left
        for num in nums:
            target = num - previous
            idx = bisect_left(primes, target)
            if idx > 0:
                previous = num - primes[idx - 1]
            else:
                return False
            print(previous)
        return True


nums = [4,9,6,10]
nums = [6,8,11,12]
nums = [5,8,3]
nums = [998, 2]

solution = Solution()
print(solution.primeSubOperation(nums))
