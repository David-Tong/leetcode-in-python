class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1) + 1
        N = len(word2) + 1
        # dp[x][y] - minimal edit distance to convert word1[:x] to word2[:y]
        dp = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if x == 0:
                    dp[x][y] = y
                    continue
                if y == 0:
                    dp[x][y] = x
                    continue
                if word1[x-1] == word2[y-1]:
                    dp[x][y] = dp[x-1][y-1]
                else:
                    dp[x][y] = min(dp[x-1][y-1], min(dp[x][y-1], dp[x-1][y])) + 1
        return dp[M-1][N-1]


word1 = "horse"
word2 = "ros"

word1 = "intention"
word2 = "execution"

word1 = ""
word2 = ""

solution = Solution()
print(solution.minDistance(word1, word2))
