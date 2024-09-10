class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # dp init
        # dp[x][y][z] - count of increasing or decreasing y team of size z, for rating[:x-1]
        #          y  - 0 for increasing and 1 for decreasing
        #          z  - z for 0, 1, 2, for team of size 1, 2, 3
        L = len(rating)
        Y = 2
        Z = 3
        dp = [[[0] * Z for _ in range(Y)] for _ in range(L)]
        for x in range(L):
            dp[x][0][0] = 1
            dp[x][1][0] = 1

        # dp transfer
        for x in range(1, L):
            for y in range(x):
                if rating[y] < rating[x]:
                    dp[x][0][1] += dp[y][0][0]
                    dp[x][0][2] += dp[y][0][1]
                else:
                    dp[x][1][1] += dp[y][1][0]
                    dp[x][1][2] += dp[y][1][1]

        # post-process
        ans = 0
        for x in range(L):
            ans += dp[x][0][2]
            ans += dp[x][1][2]
        return ans


rating = [2,5,3,4,1]
rating = [2,1,3]
rating = [1,2,3,4]
rating = [1,4,5,2,3,6,7,9,10]

solution = Solution()
print(solution.numTeams(rating))
