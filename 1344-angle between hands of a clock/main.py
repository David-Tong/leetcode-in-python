class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # pre-process
        if hour == 12:
            hour = 0
        hour_hand = ((hour * 60 + minutes) * 1.0) / (12 * 60)
        minutes_hand = (minutes * 1.0) / 60
        # print(hour_hand, minutes_hand)

        # process
        maxi = max(hour_hand, minutes_hand)
        mini = min(hour_hand, minutes_hand)
        angle = min(maxi - mini, mini + 1 - maxi)
        ans = angle * 360
        return ans


hour = 12
minutes = 30

hour = 3
minutes = 30

hour = 3
minutes = 15

hour = 1
minutes = 59

solution = Solution()
print(solution.angleClock(hour, minutes))
