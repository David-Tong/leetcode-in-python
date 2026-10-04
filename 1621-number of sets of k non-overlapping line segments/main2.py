class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7

        # process
        # dp init
        # dp[k][x] - number of sets of k + 1 non-overlapping line segments, ended with xth point
        dp = [[0] * n for _ in range(k)]
        for x in range(n):
            dp[0][x] = x

        # dp transfer
        for z in range(1, k):
            for x in range(z, n):
                for y in range(z - 1, x):
                    dp[z][x] = (dp[z][x] + dp[z - 1][y] * (x - y)) %MODULO
        # print(dp)

        ans = sum(dp[k - 1]) % MODULO
        return ans


n = 4
k = 2

n = 3
k = 1

n = 30
k = 7

solution = Solution()
print(solution.numberOfSets(n, k))