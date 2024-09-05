class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        N = len(days)
        M = 4

        # dp[x][y] - xth day in days
        #       y  - for 0, minimum costs without day pass, at xth day
        #          - for 1, minimum costs with 1-day pass, at xth day
        #          - for 2, minimum costs with 7-day pass, at xth day
        #          - for 3, minimum costs with 30-day pass, at xth day
        dp = [[float("inf")] * M for _ in range(N)]
        dp[0][1] = costs[0]
        dp[0][2] = costs[1]
        dp[0][3] = costs[2]

        for x in range(1, N):
            y = x - 1
            while y >= 0:
                # update dp[x][0]
                if days[y] + 7 > days[x]:
                    dp[x][0] = min(dp[x][0], min(dp[y][2], dp[y][3]))
                elif days[y] + 30 > days[x]:
                    dp[x][0] = min(dp[x][0], dp[y][3])
                else:
                    break
                y -= 1

            # update dp[x][1]
            for y in range(M):
                dp[x][1] = min(dp[x][1], dp[x-1][y])
            dp[x][1] += costs[0]

            # update dp[x][2], dp[x][3]
            dp[x][2] = min(dp[x][0], dp[x][1] - costs[0]) + costs[1]
            dp[x][3] = min(dp[x][0], dp[x][1] - costs[0]) + costs[2]

        print(dp)
        ans = float("inf")
        for x in range(M):
            ans = min(ans, dp[-1][x])
        return ans


days = [1,4,6,7,8,20]
costs = [2,7,15]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
costs = [3,13,45]

solution = Solution()
print(solution.mincostTickets(days, costs))
