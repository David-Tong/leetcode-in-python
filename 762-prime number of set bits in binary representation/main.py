class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19]

        def countOnes(number):
            ones = 0
            while number:
                if number & 1:
                    ones += 1
                number >>= 1
            return ones

        ans = 0
        for number in range(left, right + 1):
            ones = countOnes(number)
            if ones in primes:
                ans += 1
        return ans


left = 6
right = 10

left = 10
right = 15

solution = Solution()
print(solution.countPrimeSetBits(left, right))
