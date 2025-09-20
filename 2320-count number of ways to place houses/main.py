class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp init
        # dp[x][state] - the number of ways to place houses with the xth plots taken by state s
        #       state  - the combination of plots taken
        #                00 none of plots is taken, 01 the down plot is taken
        #                10 the upper plot is taken, 11 both plots are taken
        L = 2 ** 2
        MODULO = 10 ** 9 + 7
        dp = [[0] * L for x in range(n)]
        for state in range(L):
            dp[0][state] = 1

        # dp transfer
        # dp[x][state] - sum(dp[x - 1][other state])
        for x in range(1, n):
            for state in range(L):
                for pre_state in range(L):
                    if state & pre_state == 0:
                        dp[x][state] = (dp[x][state] + dp[x - 1][pre_state]) % MODULO
        ans = sum(dp[n - 1]) % MODULO
        return ans


n = 1
n = 2
n = 100
n = 5683
n = 10000

solution = Solution()
print(solution.countHousePlacements(n))
