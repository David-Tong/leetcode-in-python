class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # pre-process
        L = len(stones)
        presum = [0]
        for stone in stones:
            presum.append(presum[-1] + stone)

        def stoneSum(x, y):
            return presum[y + 1] - presum[x]

        # init dp
        dp = [[float("-inf")] * (L) for _ in range(L)]
        dp[0][L - 1] = 0

        # dp transfer
        # dp[x][y] - the maxi difference for stone[x : y + 1]
        # dp[x][y] = max(dp[x][y], max(stoneSum(x, y) - dp[x - 1][y], stoneSum(x, y) - dp[x][y + 1])
        ans = 0
        for k in range(L - 1, -1, -1):
            for x in range(L - k):
                if x > 0:
                    dp[x][x + k] = max(dp[x][x + k], stoneSum(x, x + k) - dp[x - 1][x + k])
                if x + k < L - 1:
                    dp[x][x + k] = max(dp[x][x + k], stoneSum(x, x + k) - dp[x][x + k + 1])
                if k == 0:
                    ans = max(ans, stoneSum(x, x + k) - dp[x][x + k])
        print(dp)
        return ans


stones = [5,3,1,4,2]

solution = Solution()
print(solution.stoneGameVII(stones))
