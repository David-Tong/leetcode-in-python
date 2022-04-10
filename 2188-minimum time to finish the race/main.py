class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        N = len(tires)
        M = len(numLaps) + 1
        # dp[x] - mini seconds to finish x laps
        # dp_tires[x][y] - the time to use the tire to finish the xth lap
        dp = [[0] * N]
        dp_tires = [[0] * N for _ in range(N) for _ in range(M)]
        dp[0][0] = 0
        for idx, tire in enumerate(tires):
            dp_tires[0][idx] = tire



