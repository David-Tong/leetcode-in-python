class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nextVisit)
        MODULO = 10 ** 9 + 7

        # dp init
        # dp[x] - the first day been in all rooms from 0 to x
        dp = [0] * L

        # dp transfer
        # dp[x] = dp[x - 1] + (1 + dp[x - 1] - dp[nextVisit[x]) + 1
        #       = 2 * dp[x - 1] - dp[nextVisit[x]] + 2
        for x in range(1, L):
            dp[x] = (2 * dp[x - 1] - dp[nextVisit[x - 1]] + 2) % MODULO
        print(dp)
        ans = dp[L - 1]
        return ans


nextVisit = [0,0]
nextVisit = [0,0,2]
nextVisit = [0,1,2,0]
nextVisit = [0,0,0,2]
nextVisit = [0,0,1,2]

solution = Solution()
print(solution.firstDayBeenInAllRooms(nextVisit))
