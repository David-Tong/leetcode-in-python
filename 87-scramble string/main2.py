class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        if len(s1) == 0:
            return True

        if s1 == s2:
            return True

        # dp[x][y][l] - if s1[x:] and s2[y:] with length of l can scramble
        L = len(s1)
        dp = [[[False] * (L + 1) for y in range(L)] for x in range(L)]

        # init
        for x in range(L):
            for y in range(L):
                dp[x][y][0] = True
                if s1[x] == s2[y]:
                    dp[x][y][1] = True

        # transfer
        for l in range(2, L + 1):
            for x in range(L - l + 1):
                for y in range(L - l + 1):
                    for k in range(1, L):
                        dp[x][y][l] = dp[x][y][l] or \
                                      (dp[x][y][k] and dp[x + k][y + k][l - k]) or \
                                      (dp[x][y + l - k][k] and dp[x + k][y][l - k])
        return dp[0][0][L]


s1 = "great"
s2 = "rgeat"

s1 = "abcde"
s2 = "caebd"

s1 = "a"
s2 = "a"

s1 = "abcdbdacbdac"
s2 = "bdacabcdbdac"

"""
s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
"""

s1 = "ackbdflwqhqarscoepmmxyymcarbjn"
s2 = "mphoebfamrmcscdblwryqykaaqjcnx"

solution = Solution()
print(solution.isScramble(s1, s2))