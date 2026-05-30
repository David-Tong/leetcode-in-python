class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        odd_sum = (1 + 2 * n - 1) * n // 2
        even_sum = (2 + 2 * n) * n // 2
        print(odd_sum, even_sum)

        # helper function
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # process
        ans = gcd(odd_sum, even_sum)
        return ans


solution = Solution()
print(solution.gcdOfOddEvenSums(5))
