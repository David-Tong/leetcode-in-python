class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # dp[x][y][z] - the number of way to build array with length for x + 1
        #                   and with the max value of the array for y
        #                   and with the search cost for z
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n)]
        for y in range(1, m + 1):
            dp[0][y][1] = 1

        # transfer
        for x in range(1, n):
            for y in range(1, m + 1):
                for z in range(1, k + 1):
                    # case 1 : if the arr[x] is the only max value of the array for y
                    # dp[x][y][z] = sum(dp[x - 1][1 ... y - 1][z - 1]
                    for t in range(1, y):
                        dp[x][y][z] = (dp[x][y][z] + dp[x - 1][t][z - 1]) % MODULO

                    # case 2 : if the arr[x] is not the only max value of the array for y
                    # dp[x][y][z] = dp[x - 1][y][z] * y
                    dp[x][y][z] = (dp[x][y][z] + dp[x - 1][y][z] * y) % MODULO

        ans = 0
        for y in range(1, m + 1):
            ans = (ans + dp[n - 1][y][z]) % MODULO

        return ans % MODULO


n = 2
m = 3
k = 1

n = 5
m = 2
k = 3

n = 9
m = 1
k = 1

n = 50
m = 100
k = 25

solution = Solution()
print(solution.numOfArrays(n, m, k))
