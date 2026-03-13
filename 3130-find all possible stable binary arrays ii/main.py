class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        M = zero + 1
        N = one + 1

        # process
        # dp init
        # dp[x][y][z] - the number of stable arrays
        #             - with x zeros and y ones
        #             - ended with z equal to zero or one
        dp = [[[0] * 2 for _ in range(N)] for _ in range(M)]
        for x in range(M):
            for y in range(N):
                for z in range(2):
                    if x == 0:
                        if y <= limit and z == 1:
                            dp[x][y][z] = 1
                    if y == 0:
                        if x <= limit and z == 0:
                            dp[x][y][z] = 1

        # dp transfer
        # dp[x][y][0] = dp[x - 1][y][0] + dp[x - 1][y][1] - dp[x - limit - 1][y][1] if x > limit
        # dp[x][y][1] = dp[x][y - 1][1] + dp[x][y - 1][1] - dp[x][y - limit - 1][0] if y > limit
        for x in range(1, M):
            for y in range(1, N):
                dp[x][y][0] = dp[x - 1][y][0] + dp[x - 1][y][1]
                if x > limit:
                    dp[x][y][0] -= dp[x - limit - 1][y][1]
                dp[x][y][1] = dp[x][y - 1][0] + dp[x][y - 1][1]
                if y > limit:
                    dp[x][y][1] -= dp[x][y - limit - 1][0]
                dp[x][y][0] %= MODULO
                dp[x][y][1] %= MODULO

        ans = (dp[zero][one][0] + dp[zero][one][1]) % MODULO
        return ans


zero = 1
one = 1
limit = 2

zero = 1
one = 2
limit = 1

zero = 3
one = 3
limit = 2

zero = 1000
one = 1000
limit = 50

solution = Solution()
print(solution.numberOfStableArrays(zero, one, limit))
