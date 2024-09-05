class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def calcDifference(timePoint, timePoint2):
            hour, minute = timePoint.split(":")
            hour2, minute2 = timePoint2.split(":")
            return (int(hour2) - int(hour)) * 60 + (int(minute2) - int(minute))

        timePoints = sorted(timePoints)
        ans = float("inf")
        for x in range(1, len(timePoints)):
            ans = min(ans, calcDifference(timePoints[x - 1], timePoints[x]))

        ans = min(ans, calcDifference("00:00", timePoints[0]) + calcDifference(timePoints[-1], "24:00"))
        return ans


timePoints = ["23:59","00:00"]
timePoints = ["00:00","23:59","00:00"]
timePoints = ["23:59","04:52","12:00","07:05","17:15","00:00"]
timePoints = ["23:59","04:52","12:00","07:05","17:15"]

solution = Solution()
print(solution.findMinDifference(timePoints))
