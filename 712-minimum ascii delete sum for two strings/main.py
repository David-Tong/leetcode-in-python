class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        N = len(s1) + 1
        M = len(s2) + 1

        # dp[x][y] - minimum delete to make s1[:x] == s2[:y]
        dp = [[0] * M for _ in range(N)]
        for x in range(N):
            for y in range(M):
                if x == 0 and y == 0:
                    dp[x][y] = 0
                    continue

                if x == 0:
                    dp[x][y] = dp[x][y-1] + ord(s2[y-1])
                    continue

                if y == 0:
                    dp[x][y] = dp[x-1][y] + ord(s1[x-1])
                    continue

                # don't delete anything
                if s1[x-1] == s2[y-1]:
                    dp[x][y] = dp[x-1][y-1]
                else:
                    # delete s1[x-1] or s2[y-1]
                    dp[x][y] = min(dp[x-1][y] + ord(s1[x-1]), dp[x][y-1] + ord(s2[y-1]))
        return dp[N-1][M-1]


s1 = "sea"
s2 = "eat"

s1 = "delete"
s2 = "leet"

#s1 = "ab"
#s2 = "cd"

#s1= "a"
#s2 = "b"

s1 = "sjfqkfxqoditw"
s2 = "fxymelgo"

solution = Solution()
print(solution.minimumDeleteSum(s1, s2))
