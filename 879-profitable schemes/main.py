class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        M = len(profit)
        N = n

        from collections import defaultdict
        # dp[x][y][z] - the number of schemes to get z profits after xth crimes with y members
        dp = [[defaultdict(int) for _ in range(N + 1)] for _ in range(M)]

        for x in range(M):
            if x == 0:
                dp[x][0][0] = 1
                if group[x] <= N:
                    dp[x][group[x]][profit[x]] = 1
            else:
                for y in range(N + 1):
                    if len(dp[x - 1][y]) > 0:
                        for z in dp[x - 1][y]:
                            dp[x][y][z] += dp[x - 1][y][z]
                            if y + group[x] <= n:
                                dp[x][y + group[x]][z + profit[x]] += dp[x - 1][y][z]

        ans = 0
        for schemes in dp[M - 1]:
            for scheme, number in schemes.items():
                if scheme >= minProfit:
                    ans += number
        return ans % MODULO


n = 5
minProfit = 3
group = [2,2]
profit = [2,3]

"""
n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]

n = 1
minProfit = 10
group = [2, 7]
profit = [6, 12]

n = 1
minProfit = 1
group = [1,1,1,1,2,2,1,2,1,1]
profit = [0,1,0,0,1,1,1,0,2,2]
"""

solution = Solution()
print(solution.profitableSchemes(n, minProfit, group, profit))
