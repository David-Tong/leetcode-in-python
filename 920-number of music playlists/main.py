class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for x in range(goal):
            for y in range(n):
                dp[x + 1][y + 1] += dp[x][y] * (n - y)
                dp[x + 1][y + 1] += dp[x][y + 1] * max(y + 1 - k, 0)
                dp[x + 1][y + 1] %= MODULO

        return dp[goal][n] % MODULO


n = 3
goal = 3
k = 1

n = 2
goal = 3
k = 0

n = 2
goal = 3
k = 1

solution = Solution()
print(solution.numMusicPlaylists(n, goal, k))
