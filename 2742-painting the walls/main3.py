class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        L = len(cost)

        # dp[x][y] - the minimal cost to hire painter to paint x wall and can paint y wall with free painter
        old = [float("inf")] * (L + 1)
        old[0] = 0

        # transfer
        for x in range(L):
            new = [float("inf")] * (L + 1)
            for y in range(L + 1):
                new[y] = old[y]
            for y in range(L + 1):
                new[min(L, y + 1 + time[x])] = min(new[min(L, y + 1 + time[x])], old[y] + cost[x])
            old = new

        # ans
        return old[L]


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
