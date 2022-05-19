class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[x][y] - (x + 1) length vowel string, begun with yth vowel ordered by (u, o, i, e, a)
        dp = [[0] * 5 for _ in range(n)]
        for y in range(5):
            dp[0][y] = y + 1

        for x in range(1, n):
            for y in range(0, 5):
                for z in range(0, y + 1):
                    dp[x][y] += dp[x - 1][z]

        return dp[n-1][4]


n = 1
n = 2
n = 3
n = 33
n = 50

solution = Solution()
print(solution.countVowelStrings(n))
