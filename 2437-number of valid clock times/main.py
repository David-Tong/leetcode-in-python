class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        # pre-process
        hour, minute = time.split(":")

        # process
        if hour[0] == "?" and hour[1] == "?":
            hours = 24
        elif hour[0] == "?":
            if hour[1] > "3":
                hours = 2
            else:
                hours = 3
        elif hour[1] == "?":
            if hour[0] > "1":
                hours = 4
            else:
                hours = 10
        else:
            hours = 1

        if minute[0] == "?" and minute[1] == "?":
            minutes = 60
        elif minute[0] == "?":
            minutes = 6
        elif minute[1] == "?":
            minutes = 10
        else:
            minutes = 1

        ans = hours * minutes
        return ans


time = "?5:00"
time = "0?:0?"
time = "??:??"
time = "?2:16"
time = "2?:??"
time = "?4:22"

solution = Solution()
print(solution.countTime(time))
