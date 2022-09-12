class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        M = len(s1) + 1
        N = len(s2) + 1
        # dp[x][y] - if s1[:x] and s2[:y] can be an interleaving string
        dp = [[False] * N for x in range(M)]

        for x in range(M):
            for y in range(N):
                if x == 0 and y == 0:
                    dp[x][y] = True
                    continue

                if x > 0 and s1[x-1] == s3[x+y-1]:
                    dp[x][y] |= dp[x-1][y]

                if y > 0 and s2[y-1] == s3[x+y-1]:
                    dp[x][y] |= dp[x][y-1]

        return dp[M-1][N-1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#s3 = "aadbbbaccc"

s1 = "a"
s2 = ""
#s3 = ""
s3 = "a"

#s1 = "abba"
#s2 = "cddc"
#s3 = "abcdbadc"

#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbcbbcac"

s1 = "db"
s2 = "b"
s3 = "cbb"

solution = Solution()
print(solution.isInterleave(s1, s2, s3))
