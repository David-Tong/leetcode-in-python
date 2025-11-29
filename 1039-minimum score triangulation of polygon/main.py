class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        # dp init
        L = len(values)
        # dp[x][y] - the minmal score for triangulation for point x to point y
        dp = [[float("inf")] * L for _ in range(L)]
        for x in range(L - 1):
            dp[x][x + 1] = 0

        # dp transfer
        for l in range(3, L + 1):
            for x in range(L - l + 1):
                y = x + l - 1
                for z in range(x + 1, y):
                    dp[x][y] = min(dp[x][y], dp[x][z] + values[x] * values[y] * values[z] + dp[z][y])
        return dp[0][L - 1]


values = [1,2,3]
values = [3,7,4,5]
values = [1,3,1,4,1,5]

solution = Solution()
print(solution.minScoreTriangulation(values))
