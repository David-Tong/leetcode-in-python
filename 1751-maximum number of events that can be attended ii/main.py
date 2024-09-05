class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        M = len(events)

        # sort
        events = sorted(events, key=lambda x: (x[1], x[0]))

        # dp - dp[x][y] - the max value when select y + 1 from x + 1 intervals
        dp = [[float("-inf")] * k for _ in range(M)]
        for x in range(M):
            dp[x][0] = 0
        dp[0][0] = events[0][2]

        # ends
        ends = list()
        for x in range(M):
            ends.append(events[x][1])

        from bisect import bisect_left
        ans = events[0][2]
        for x in range(1, M):
            start, end, value = events[x]
            idx = bisect_left(ends, start)
            for y in range(min(x + 1, k)):
                if y > 0:
                    if idx == 0:
                        dp[x][y] = max(dp[x - 1][y], value)
                    else:
                        dp[x][y] = max(dp[x - 1][y], dp[idx - 1][y - 1] + value)
                else:
                    dp[x][y] = max(dp[x - 1][y], value)
                ans = max(ans, dp[x][y])
        return ans


events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2

events = [[1,2,4],[3,4,3],[2,3,10]]
k = 2

events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
k = 3

events = [[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]]
k = 3

events = [[74,91,40]]
k = 1

events = [[0,10,20],[0,20,40],[0,30,50]]
k = 1

solution = Solution()
print(solution.maxValue(events, k))
