class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        MOD = 24
        return (arrivalTime + delayedTime) % MOD


arrivalTime = 15
delayedTime = 5

arrivalTime = 13
delayedTime = 11

solution = Solution()
print(solution.findDelayedArrivalTime(arrivalTime, delayedTime))
