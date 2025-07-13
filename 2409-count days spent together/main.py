class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # pre-process
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        presum = [0]
        for month in months:
            presum.append(presum[-1] + month)

        # process
        month_a, month_l = int(arrive.split("-")[0]), int(leave.split("-")[0])
        day_a, day_l = int(arrive.split("-")[1]), int(leave.split("-")[1])

        ans = 0
        if month_l > month_a:
            ans += presum[month_l - 1] - presum[month_a - 1]
        elif month_l < month_a:
            return 0
        ans += day_l - day_a + 1
        return ans if ans > 0 else 0


arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"

arriveAlice = "10-01"
leaveAlice = "10-31"
arriveBob = "11-01"
leaveBob = "12-31"

arriveAlice = "09-01"
leaveAlice = "12-31"
arriveBob = "11-01"
leaveBob = "12-27"

solution = Solution()
print(solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
