class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        M = len(s) + 1
        N = len(p) + 1
        dp = [[False] * N for x in range(M)]

        for x in range(M):
            for y in range(N):
                if x == 0 and y == 0:
                    dp[x][y] = True
                    continue

                if y == 0:
                    dp[x][y] = False
                    continue

                if x > 0:
                    if p[y-1] == "." or p[y-1] == s[x-1]:
                        dp[x][y] |= dp[x-1][y-1]
                    if p[y-1] == "*":
                        if p[y-2] == "." or p[y-2] == s[x-1]:
                            dp[x][y] |= dp[x-1][y]

                if p[y-1] == "*":
                    dp[x][y] |= dp[x][y-2]

        return dp[M-1][N-1]


s = "aa"
p = "a"

s = "aa"
p = "a*"

s = "ab"
p = ".*"

solution = Solution()
print(solution.isMatch(s, p))
