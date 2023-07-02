class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        L = len(timeSeries)

        ans = 0
        for x in range(1, L):
            if timeSeries[x - 1] + duration <= timeSeries[x]:
                ans += duration
            else:
                ans += timeSeries[x] - timeSeries[x - 1]
        ans += duration
        return ans


timeSeries = [1,4]
duration = 2

timeSeries = [1,2]
duration = 2

solution = Solution()
print(solution.findPoisonedDuration(timeSeries, duration))
