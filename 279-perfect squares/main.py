class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt, ceil
        if sqrt(n) == ceil(sqrt(n)):
            M = int(ceil(sqrt(n))) + 1
        else:
            M = int(ceil(sqrt(n)))

        squares = []
        for x in range(1, M):
            squares.append(x ** 2)

        N = n + 1
        dp = [float("inf")] * N
        for square in squares:
            dp[square] = 1

        for x in range(1, N):
            for square in squares:
                if x - square > 0:
                    dp[x] = min(dp[x], dp[x-square] + 1)
        return dp[N-1]


n = 12
n = 13
n = 2
n = 1
n = 3
n = 4
n = 28

solution = Solution()
print(solution.numSquares(n))
