class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        L = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        edge = total // 4

        # state dp
        dp = [-1] * (1 << L)
        dp[0] = 0
        for state in range(1, len(dp)):
            for idx, val in enumerate(matchsticks):
                if state & (1 << idx) == 0:
                    continue
                previous = state & ~(1 << idx)
                if dp[previous] >= 0 and dp[previous] + val <= edge:
                    dp[state] = (dp[previous] + val) % edge
                    break
        return dp[-1] == 0


matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
matchsticks = [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]

solution = Solution()
print(solution.makesquare(matchsticks))
