class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        N = len(values)
        dp = [0] * N
        dp[1] = values[1] + values[0] - 1
        for x in range(2, N):
            dp[x] = max(dp[x-1] - values[x-1] + values[x] - 1, values[x] + values[x-1] - 1)
        return max(dp)


values = [8, 1, 5, 2, 6]
values = [1,2]
values = [8, 1, 5, 2, 9]


solution = Solution()
print(solution.maxScoreSightseeingPair(values))
