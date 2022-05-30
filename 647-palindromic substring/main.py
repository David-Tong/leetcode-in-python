class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        # dp[x][y] = s[x:y+1] is a palindromic string
        dp = [[False] * N for _ in range(N)]

        ans = 0
        for x in range(N - 1, -1, -1):
            for y in range(x, N, 1):
                if x == y:
                    ans += 1
                    dp[x][y] = True
                elif x + 1 == y:
                    if s[x] == s[y]:
                        ans += 1
                        dp[x][y] = True
                else:
                    if s[x] == s[y]:
                        if dp[x+1][y-1]:
                            ans += 1
                            dp[x][y] = True
        return ans


s = "abc"
s = "aaa"
s = "babad"
s = "cbbd"
s = "cbabadabab"
s = "a"
s = "mississippi"

solution = Solution()
print(solution.countSubstrings(s))
