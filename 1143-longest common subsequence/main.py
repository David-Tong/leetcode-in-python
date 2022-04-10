class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        M = len(text1) + 1
        N = len(text2) + 1
        # dp[x][y] - longest common subsequence for text1[:x] and text2[:y]
        dp = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                if x == 0:
                    continue
                if y == 0:
                    continue
                if text1[x-1] == text2[y-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                else:
                    dp[x][y] = max(dp[x][y-1], dp[x-1][y])
        return dp[M-1][N-1]


text1 = "abcde"
text2 = "ace"

text1 = "abc"
text2 = "abc"

text1 = "abc"
text2 = "def"

text1 = "aec"
text2 = "ac"

text1 = "aecf"
text2 = "acw"

solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))
