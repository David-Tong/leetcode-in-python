class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        L = len(piles)

        # calculate presums
        presums = list()
        capacities = list()
        capacity = 0
        for pile in piles:
            presum = list()
            presum.append(0)
            capacity += len(pile)
            for coin in pile:
                presum.append(presum[-1] + coin)
            presums.append(presum)
            capacities.append(capacity)

        # dp[x][y] - the max value of coins after xth piles with y coins taken
        dp = [[-1] * (k + 1) for _ in range(L)]
        for x in range(L):
            if x == 0:
                for y in range(min(capacities[x], k) + 1):
                    dp[x][y] = presums[x][y]
            else:
                for y in range(min(capacities[x], k) + 1):
                    for z in range(len(piles[x]), -1, -1):
                        if y - z >= 0:
                            if dp[x - 1][y - z] >= 0:
                                dp[x][y] = max(dp[x][y], dp[x - 1][y - z] + presums[x][z])
                            else:
                                break
        return dp[L - 1][k]


piles = [[1,100,3],[7,8,9]]
k = 2

piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
k = 7

piles = [[100]]
k = 1

solution = Solution()
print(solution.maxValueOfCoins(piles, k))
