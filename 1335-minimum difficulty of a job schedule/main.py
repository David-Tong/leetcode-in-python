class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        L = len(jobDifficulty)

        # pre-process
        maxi = [[0] * (L + 1) for _ in range(L + 1)]
        for x in range(L + 1):
            for y in range(x + 1, L + 1):
                maxi[x][y] = max(jobDifficulty[x:y])

        # dp[x][y] - the minimal difficulty after x day and complete the first y jobs, jobDifficulty[:y]
        dp = [[float("inf")] * (L + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        for x in range(d):
            for y in range(L + 1):
                for z in range(y):
                    dp[x + 1][y] = min(dp[x + 1][y], maxi[z][y] + dp[x][z])
        return -1 if dp[d][L] == float("inf") else dp[d][L]


jobDifficulty = [6,5,4,3,2,1]
d = 2

jobDifficulty = [9,9,9]
d = 4

jobDifficulty = [1,1,1]
d = 3

jobDifficulty = [10,9,8,7,6,5,4,3,2,1,11]
d = 7

jobDifficulty = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
d = 10

solution = Solution()
print(solution.minDifficulty(jobDifficulty, d))
