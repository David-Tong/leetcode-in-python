class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        # dp[k][i][ci] - k group, ith house, and cith color, target * m * n
        # dp[k][i][ci] = min(dp[k-(ci!=cj)][j][cj]) + cost[i][ci] if colors[i] == 0 else 0, j = i-1
        # dp[k][i][ci] - k group, ith house, and cith color, target * m * n
        # dp[k][i][ci] = min(dp[k-(ci!=cj)][j][cj]) + cost[i][ci] if colors[i] == 0 else 0, j = i-1
        dp = [[[float("inf")] * (n + 1) for _ in range(m + 1)] for _ in range(target + 1)]
        for ci in range(n + 1):
            dp[0][0][ci] = 0

        for k in range(1, target + 1):
            for i in range(k, m + 1):
                hi = houses[i - 1]
                hj = houses[i - 2] if i >= 2 else 0
                (si, ei) = (hi, hi + 1) if hi else (1, n + 1)
                (sj, ej) = (hj, hj + 1) if hj else (1, n + 1)
                for ci in range(si, ei):
                    v = 0 if ci == hi else cost[i - 1][ci - 1]
                    for cj in range(sj, ej):
                        dp[k][i][ci] = min(dp[k][i][ci], dp[k - (ci != cj)][i - 1][cj] + v)

        ans = min(dp[target][m])
        return -1 if ans == float("inf") else ans


houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3

"""
houses = [0,2,1,2,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3

houses = [3,1,2,3]
cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
m = 4
n = 3
target = 3
"""

solution = Solution()
print(solution.minCost(houses, cost, m, n, target))
