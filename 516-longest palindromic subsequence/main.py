class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        # dp[x][y] - longest palindrome subsequence length in s[x:y+1]
        dp = [[0] * N for _ in range(N)]

        # dp[x][y] = dp[x+1][y-1] + 2 if s[x] == s[y]
        #          = y - x + 1 if s[x] == s[y] and y - x + 1 < 3
        for x in range(N-1, -1, -1):
            dp[x][x] = 1
            for y in range(x+1, N, 1):
                if s[x] == s[y]:
                    if y - x + 1 < 3:
                        dp[x][y] = y - x + 1
                    else:
                        dp[x][y] = dp[x+1][y-1] + 2
                else:
                    dp[x][y] = max(dp[x+1][y], dp[x][y-1])

        return dp[0][N-1]


s = "bbbab"
s = "cbbd"
s = "bbcabcabbc"
s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"

solution = Solution()
print(solution.longestPalindromeSubseq(s))
