class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pre-process
        DIVISORS = [3, 5, 7]

        # process
        ans = 0
        for x in range(n):
            for divisor in DIVISORS:
                if (x + 1) % divisor == 0:
                    ans += x + 1
                    break
        return ans


n = 7
n = 10
n = 9

solution = Solution()
print(solution.sumOfMultiples(n))
