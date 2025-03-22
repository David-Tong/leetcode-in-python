class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # pre-process
        M = len(str1)
        N = len(str2)

        # solve LCS
        # dp[x][y] - LCS length for str1[:x] and str2[:y]
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for x in range(M):
            for y in range(N):
                if str1[x] == str2[y]:
                    dp[x + 1][y + 1] = dp[x][y] + 1
                else:
                    dp[x + 1][y + 1] = max(dp[x][y + 1], dp[x + 1][y])
        # print(dp)

        # process
        x, y = M, N
        ans = list()
        while x or y:
            ch = '';
            # case 1
            #   if x == 0 then ch = str2[--y]
            if x == 0:
                y -= 1
                ch = str2[y]
            # case 2
            #   if y == 0 then ch = str1[--x]
            elif y == 0:
                x -= 1
                ch = str1[x]
            # case 3
            #   if str1[x - 1] == str2[y - 1] then ch = str1[--x] = str2[--y]
            elif str1[x - 1] == str2[y - 1]:
                x -= 1
                y -= 1
                ch = str1[x]
            # case 4
            #   if dp[x - 1][y] == dp[x][y] then ch = str1[--x]
            elif dp[x - 1][y] == dp[x][y]:
                x -= 1
                ch = str1[x]
            # case 5
            #   if dp[x][y - 1] == dp[x][y] then ch = str2[--y]
            elif dp[x][y - 1] == dp[x][y]:
                y -= 1
                ch = str2[y]
            ans.append(ch)

        return "".join(ans[::-1])


str1 = "abac"
str2 = "cacbc"

str1 = "abac"
str2 = "cab"

str1 = "aaaaaaaa"
str2 = "aaaaaaaa"

str1 = "abc"
str2 = "xyz"

solution = Solution()
print(solution.shortestCommonSupersequence(str1, str2))
