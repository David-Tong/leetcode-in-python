class Solution(object):
    def minCost(self, n, cost):
        """
        :type n: int
        :type cost: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = (n + 1) // 2
        M = len(cost[0])

        # dp init
        # dp[x][y][z] - the minimum cost to pain x and n - 1 - x houses beautifully
        #       y, z - the color combination to pain x and n - 1 - x houses
        #       0, 1 - paint house x with color 0 and house n - 1 -x with color 1
        dp = [[[float("inf")] * M for _ in range(M)] for _ in range(L)]
        for y in range(M):
            for z in range(M):
                if y != z:
                    dp[0][y][z] = cost[0][y] + cost[n - 1][z]

        # dp transfer
        # dp[x][y][z] = min(dp[x-1][y'][z']) if y' != y and z' != z and y != z
        for x in range(1, L):
            for y in range(M):
                for z in range(M):
                    for yp in range(M):
                        for zp in range(M):
                            if y != z and y != yp and z != zp:
                                dp[x][y][z] = min(dp[x][y][z], dp[x - 1][yp][zp] + cost[x][y] + cost[n - 1 - x][z])
        # print(dp)

        # post-process
        ans = float("inf")
        for y in range(M):
            for z in range(M):
                ans = min(ans, dp[L - 1][y][z])
        return ans


n = 4
cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]

n = 6
cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]

n = 1000
from random import randint
cost = [[randint(0, 100000) for _ in range(3)] for _ in range(n)]
print(cost)

solution = Solution()
print(solution.minCost(n, cost))
