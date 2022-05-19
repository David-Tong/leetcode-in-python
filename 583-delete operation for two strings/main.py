class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        M = len(word1) + 1
        N = len(word2) + 1
        # dp[x][y] - minimum deletion to make word1[:x] and word2[:y] equal
        dp = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if x == 0 and y == 0:
                    dp[x][y] = 0
                elif x == 0:
                    dp[x][y] = dp[x][y-1] + 1
                elif y == 0:
                    dp[x][y] = dp[x-1][y] + 1
                else:
                    if word1[x-1] == word2[y-1]:
                        dp[x][y] = dp[x-1][y-1]
                    else:
                        dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + 1
        return dp[M-1][N-1]


word1 = "sea"
word2 = "eat"

word1 = "leetcode"
word2 = "etco"

solution = Solution()
print(solution.minDistance(word1, word2))
