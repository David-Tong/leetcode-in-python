class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        # helper function
        # quick pow
        def quickPow(x, N):
            if N == 0:
                return 1

            y = quickPow(x, N // 2)
            return y * y % MODULO if N % 2 == 0 else y * y % MODULO * x % MODULO

        # get factorials
        def factorial(N):
            factorials = list()
            factorials.append(1)
            for x in range(N):
                factorials.append(factorials[-1] * (x + 1) % MODULO)
            return factorials

        factorials = factorial(n)

        # combination
        def combination(M, N):
            if N > M:
                return 0
            a = factorials[M]
            b = factorials[N] * factorials[M - N] % MODULO
            inv_b = quickPow(b, MODULO - 2)

            return a * inv_b % MODULO

        # process
        # the counts to place exactly k matching adjacent elements in an array of size n
        #   for element in the inclusive range [1, m]
        # x [x x] x x [x x] x [x x]
        # x [x x x] x x x [x x] x
        counts = m * pow(m - 1, n - k - 1) % MODULO

        # the combination to select k matching adjacent elments in an array of size n
        comb = combination(n - 1, k) % MODULO

        ans = counts * comb % MODULO
        return ans


n = 3
m = 2
k = 1

n = 4
m = 2
k = 2

n = 5
m = 2
k = 0

n = 40603
m = 16984
k = 29979

solution = Solution()
print(solution.countGoodArrays(n, m, k))
