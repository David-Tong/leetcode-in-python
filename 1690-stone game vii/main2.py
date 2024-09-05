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

        # dp[x][y] - the maxi difference for stone[x : y + 1]
        # dp[x][y] = max(dp[x][y], max(stoneSum(x, y) - dp[x + 1][y], stoneSum(x, y) - dp[x][y - 1])
        dp = [[0] * L for _ in range(L)]
        for k in range(1, L, 1):
            l = 0
            r = l + k
            while r < L:
                dp[l][r] = max(stoneSum(l + 1, r) - dp[l + 1][r], stoneSum(l, r - 1) - dp[l][r - 1])
                l += 1
                r += 1
        return dp[0][L - 1]


stones = [5,3,1,4,2]
#stones = [7,90,5,1,100,10,10,2]

solution = Solution()
print(solution.stoneGameVII(stones))
