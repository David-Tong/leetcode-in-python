class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        M = len(s) + 1
        N = len(t) + 1
        # dp[x][y] - s[:x+1] is a subsequence of t[:y+1]
        dp = [[False] * N for _ in range(M)]
        dp[0][0] = True

        for x in range(M):
            for y in range(N):
                if x == 0:
                    dp[x][y] = True
                    continue
                if y > 0:
                    dp[x][y] |= dp[x][y-1]
                    if s[x-1] == t[y-1]:
                        dp[x][y] |= dp[x-1][y-1]
        return dp[M-1][N-1]


s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"

s = "abc"
t = "ahbgd"

s = "abc"
t = "ab"

s = ""
t = ""

s = "a"
t = "a"

solution = Solution()
print(solution.isSubsequence(s, t))
