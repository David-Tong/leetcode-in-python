class Solution(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        def doDelete(substring, dp, idx):
            S = len(substring)
            middle = S / 2
            for x in range(middle):
                if substring[: x + 1] == substring[x + 1: 2 * x + 2]:
                    dp[idx] = max(dp[idx], dp[S - 1 - (x + 1)] + 1)

        L = len(s)
        # dp[x] - the number of s[L - x - 1:] maximum deletions
        dp = [1] * L

        for x in range(L - 1, -1, -1):
            doDelete(s[x:], dp, L - 1 - x)

        return dp[L - 1]


s = "abcabcdabc"
s = "aaabaab"
s = "aaaaa"
s = "aaabaaa"

solution = Solution()
print(solution.deleteString(s))
