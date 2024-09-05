class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        L = len(cost)

        # dp[x][y] - the minimal cost to paint x walls, with y buffer to hire free painters
        from collections import defaultdict
        dp = list()
        for x in range(L + 1):
            dp.append(defaultdict(float))
        dp[0][0] = 0

        # transfer
        for x in range(L):
            for y in dp[x].keys():
                # use free painter
                if y - 1 not in dp[x + 1]:
                    dp[x + 1][y - 1] = float("inf")
                dp[x + 1][y - 1] = min(dp[x + 1][y - 1], dp[x][y])

                # use paid painter
                if min(L, y + time[x]) not in dp[x + 1]:
                    dp[x + 1][min(L, y + time[x])] = float("inf")
                dp[x + 1][min(L, y + time[x])] = min(dp[x + 1][min(L, y + time[x])], dp[x][y] + cost[x])

        ans = float("inf")
        for y in dp[L].keys():
            if y >= 0:
                ans = min(ans, dp[L][y])

        return ans


cost = [1,2,3,2]
time = [1,2,3,2]

cost = [2,3,4,2]
time = [1,1,1,1]

cost = [3,4,5,6,1,2,3,5,6,8]
time = [5,4,1,2,1,2,1,1,1,2]

cost = [8,7,5,15]
time = [1,1,2,1]

solution = Solution()
print(solution.paintWalls(cost, time))
