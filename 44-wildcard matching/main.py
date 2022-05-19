class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        M = len(s) + 1
        N = len(p) + 1
        # dp[x][y] - if s[:x] and p[:y] are matching
        dp = [[False] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                if x == 0 and y == 0:
                    dp[x][y] = True
                elif x == 0:
                    if p[y-1] == "*":
                        dp[x][y] = dp[x][y-1]
                elif y == 0:
                    dp[x][y] = False
                else:
                    if s[x-1] == p[y-1] or p[y-1] == "?":
                        dp[x][y] = dp[x-1][y-1]
                    elif p[y-1] == "*":
                        dp[x][y] = dp[x-1][y-1] | dp[x-1][y] | dp[x][y-1]
        return dp[M-1][N-1]


s = "aa"
p = "a"

s = "aa"
p = "*"

s = "cb"
p = "?a"

s = ""
p = ""

s = "abc"
p = ""

s = "adceb"
p = "*a*b"

s = "abcabczzzde"
p = "*abc???de*"

solution = Solution()
print(solution.isMatch(s, p))
