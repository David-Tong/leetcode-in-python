class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # dp init
        # dp[x][0] - the deletions to make s[:x+1] all 'a's
        # dp[x][1] - the deletions to make s[x:] all 'b' s
        dp = [[0] * 2 for _ in range(L)]

        # dp transfer
        for x in range(L):
            if s[x] == 'a':
                if x != 0:
                    dp[x][0] = dp[x-1][0]
            else:
                if x == 0:
                    dp[x][0] = 1
                else:
                    dp[x][0] = dp[x-1][0] + 1

        for x in range(L - 1, -1, -1):
            if s[x] == 'b':
                if x != L - 1:
                    dp[x][1] += dp[x+1][1]
            else:
                if x == L - 1:
                    dp[x][1] = 1
                else:
                    dp[x][1] = dp[x+1][1] + 1

        # process
        ans = float("inf")
        for x in range(L):
            if x == 0:
                ans = min(ans, dp[x][1])
            else:
                ans = min(ans, dp[x-1][0] + dp[x][1])
        ans = min(ans, dp[L-1][0])
        return ans


s = "aababbab"
s = "bbaaaaabb"
s = "bbbbbbbaaa"

solution = Solution()
print(solution.minimumDeletions(s))
