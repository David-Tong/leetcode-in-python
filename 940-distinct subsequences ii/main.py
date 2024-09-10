class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        # dp init
        # dp[c] - distinct subsequences ended with character 'c'
        dp = [0] * 26

        # dp transfer
        for c in s:
            idx = ord(c) - ord('a')
            dp[idx] = (1 + sum(dp)) % MODULO

        ans = sum(dp) % MODULO
        return ans


s = "abc"
s = "aba"
s = "aaa"

solution = Solution()
print(solution.distinctSubseqII(s))
