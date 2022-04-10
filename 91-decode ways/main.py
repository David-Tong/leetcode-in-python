class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s) + 1
        dp = [0] * N
        dp[0] = 1

        for x in range(1, N):
            if int(s[x-1:x]) > 0:
                dp[x] += dp[x-1]
            if x >= 2:
                if int(s[x-2:x]) > 0 and int(s[x-2:x]) <= 26:
                    if s[x-2] != "0":
                        dp[x] += dp[x-2]
        return dp[N - 1]


s = "12"
s = "226"
s = "06"
s = "10"
s = "110"


solution = Solution()
print(solution.numDecodings(s))
