class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [float("inf")] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for x in range(2, len(cost) + 1):
            dp[x] = min(dp[x-1] + cost[x-1], dp[x-2] + cost[x-2])
        return dp[len(cost)]


cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]


solution = Solution()
print(solution.minCostClimbingStairs(cost))
