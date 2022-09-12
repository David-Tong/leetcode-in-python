class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        VOWELS = 5
        MOD = 10 ** 9 + 7

        # dp[x][y] - the number of permutation with (x + 1) length ended with yth vowels (a, e, i, o, u)
        dp = [[0] * VOWELS for _ in range(n)]
        for y in range(VOWELS):
            dp[0][y] = 1

        for x in range(1, n):
            dp[x][0] = dp[x - 1][1] + dp[x - 1][2] + dp[x - 1][4]
            dp[x][1] = dp[x - 1][0] + dp[x - 1][2]
            dp[x][2] = dp[x - 1][1] + dp[x - 1][3]
            dp[x][3] = dp[x - 1][2]
            dp[x][4] = dp[x - 1][2] + dp[x - 1][3]

        return sum(dp[n - 1]) % MOD


n = 1
n = 2
n = 5
n = 20000

solution = Solution()
print(solution.countVowelPermutation(n))