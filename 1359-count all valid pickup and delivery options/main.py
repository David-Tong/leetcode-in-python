class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10e8 + 7
        def factorial(n):
            ans = 1
            for x in range(1, n + 1):
                ans = ans * x
                if x <= n / 2:
                    ans = ans / 2
                ans = ans % MODULO
            return ans

        n_factorial = factorial(2 * n)
        ans = int(n_factorial)
        return ans


n = 2
n = 3
n = 500

solution = Solution()
print(solution.countOrders(n))
