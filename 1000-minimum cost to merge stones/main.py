class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        L = len(stones)
        # has answer
        if (L - 1) % (k - 1):
            return -1

        # presum
        presum = [1]
        for stone in stones:
            presum.append(presum[-1] + stone)

        # dp[x][y][u] - min cost to merge subarray[i:j+1] to k piles
        dp = [[[float("inf")] * (k + 1) for _ in range(L)] for _ in range(L)]
        for x in range(L):
            dp[x][x][1] = 0

        for l in range(2, L + 1):
            for x in range(L):
                y = x + l - 1
                if y < L:
                    for u in range(2, k + 1):
                        for v in range(x, y):
                            # transfer 1 - cost to have k piles for subarray[i:j+1]
                            dp[x][y][u] = min(dp[x][y][u], dp[x][v][1] + dp[v + 1][y][u - 1])
                    # transfer 2 - merge k piles to 1
                    if dp[x][y][k] != float("inf"):
                        dp[x][y][1] = dp[x][y][k] + presum[y + 1] - presum[x]
        return dp[0][L - 1][1]


stones = [3,2,4,1]
k = 2

stones = [3,2,4,1]
k = 3

stones = [3,5,1,2,6]
k = 3

stones = [3,4,5,6,1,2,3,11,2,1,2,3,45,8,7,1,12,99,12,32]
k = 2

stones = [3,4,5,6,1,2,3,11,2,1,2,3,45,8,7,1,12,99,12,32,45,6,7,89,11,2,3,13,14,100]
k = 2

solution = Solution()
print(solution.mergeStones(stones, k))
