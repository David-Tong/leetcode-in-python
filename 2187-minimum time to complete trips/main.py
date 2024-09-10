class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def canTrip(target):
            trips = 0
            for t in time:
                trips += target // t
            if trips >= totalTrips:
                return True
            else:
                return False

        left = 1
        right = min(time) * totalTrips

        while left + 1 < right:
            middle = (left + right) // 2
            if canTrip(middle):
                right = middle
            else:
                left = middle + 1

        if canTrip(left):
            return left
        else:
            return right


time = [1,2,3]
totalTrips = 5

time = [2]
totalTrips = 1

time = [5,4,3]
totalTrips = 5

solution = Solution()
print(solution.minimumTime(time, totalTrips))
