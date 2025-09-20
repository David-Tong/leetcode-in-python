class Solution(object):
    def longestPalindromicSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)

        # dp init
        # dp[x][y][k] - the longest palindromic subsequence after k operations for s[x:y+1]
        dp = [[[0] * (k + 1) for _ in range(L)] for _ in range(L)]
        for x in range(L):
            dp[x][x][0] = 1
        # print(dp)

        # process
        # helper function
        # cost function - the minimum cost to make a pair of ch and ch2 same
        def cost(ch, ch2):
            return min((ord(ch) - ord(ch2) + 26) % 26,
                       (ord(ch2) - ord(ch) + 26) % 26)
        print(cost("o", "u"))

        # dp transfer
        # dp[x][y][z] = max(dp[x+1][y-1][z - cost] + 2, dp[x+1][y][z], dp[x][y-1][z])
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                for z in range(k + 1):
                    dp[x][y][z] = max(dp[x + 1][y][z], dp[x][y - 1][z])
                    c = cost(s[x], s[y])
                    if z - c >= 0:
                        dp[x][y][z] = max(dp[x][y][z], dp[x + 1][y - 1][z - c] + 2)

        # print(dp)
        ans = max(dp[0][L -1])
        return ans


s = "abced"
k = 2

s = "aaazzz"
k = 4

s = "adfgzz"
k = 12

"""
import string, random
s = "".join([random.choice(string.ascii_lowercase) for _ in range(200)])
k = 200
print(s)
"""

s = "ou"
k = 6

solution = Solution()
print(solution.longestPalindromicSubsequence(s, k))
