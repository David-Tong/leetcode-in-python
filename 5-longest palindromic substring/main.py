class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        # dp[x][y] - s[x:y+1] is a palindrome or not
        dp = [[False] * N for ch in s]
        left = 0
        right = 0

        # dp[x][y] - dp[x+1][y-1] & s[x] == sp[y]
        for x in range(N - 2, -1, -1):
            dp[x][x] = True
            for y in range(x + 1, N):
                if s[x] == s[y]:
                    if y - x + 1 < 3 or dp[x+1][y-1]:
                        dp[x][y] = True
                        if y - x > right - left:
                            right = y
                            left = x
        return s[left:right + 1]

s = "babad"
s = "cbbd"
s = "cbabadabab"
s = "a"
s = "cbc9119119"

solution = Solution()
print(solution.longestPalindrome(s))
