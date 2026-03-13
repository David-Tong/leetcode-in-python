class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        def process(num):
            from math import sqrt
            upper = int(sqrt(num))
            divisors = set()
            for x in range(1, upper + 1):
                if num % x == 0:
                    divisors.add(x)
                    divisors.add(num // x)
                if len(divisors) > 4:
                    return 0
            if len(divisors) == 4:
                return sum(divisors)
            else:
                return 0

        # process
        ans = 0
        for num in nums:
            ans += process(num)
        return ans


nums = [21,4,7]
nums = [21,21]
nums = [1,2,3,4,5]

from random import randint
nums = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
print(nums)

solution = Solution()
print(solution.sumFourDivisors(nums))
