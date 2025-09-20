class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        # dp init
        M = len(tasks)
        N = 1 << M
        # dp[x] - the minimal session to complete tasks combination of x
        dp = [float("inf")] * N

        # set init state
        for state in range(N):
            target, time, idx = state, 0, 0
            while target:
                if target & 1:
                    time += tasks[idx]
                idx += 1
                target >>= 1
            if time <= sessionTime:
                dp[state] = 1
        # print(dp)

        # dp transfer
        # dp[state] = min(dp[state], dp[subset] + dp[state - subset])
        for state in range(N):
            subset = state
            while subset:
                dp[state] = min(dp[state], dp[subset] + dp[state - subset])
                subset = (subset - 1) & state
        ans = dp[N - 1]
        return ans


tasks = [1,2,3]
sessionTime = 3

tasks = [3,1,3,1,1]
sessionTime = 8

tasks = [1,2,3,4,5]
sessionTime = 15

tasks = [1,2,3,4,5]
sessionTime = 15

solution = Solution()
print(solution.minSessions(tasks, sessionTime))
