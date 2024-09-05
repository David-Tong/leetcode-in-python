class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        def calculateRounds(loginTime, logoutTime):
            if loginTime == logoutTime:
                return 0

            loginHour, loginMinute = int(loginTime.split(":")[0]), int(loginTime.split(":")[1])
            logoutHour, logoutMinute = int(logoutTime.split(":")[0]), int(logoutTime.split(":")[1])

            rounds = 0
            if loginHour < logoutHour:
                rounds = (logoutHour - loginHour - 1) * 4 + (60 - loginMinute) // 15 + logoutMinute // 15
            else:
                if loginMinute == 0:
                    loginRounds = set([1, 2, 3, 4])
                elif loginMinute <= 15:
                    loginRounds = set([2, 3, 4])
                elif loginMinute <= 30:
                    loginRounds = set([3, 4])
                elif loginMinute <= 45:
                    loginRounds = set([4])
                else:
                    loginRounds = set()

                if logoutMinute < 15:
                    logoutRounds = set([1, 2, 3, 4])
                elif logoutMinute < 30:
                    logoutRounds = set([2, 3, 4])
                elif logoutMinute < 45:
                    logoutRounds = set([3, 4])
                else:
                    logoutRounds = set([4])

                rounds = len(loginRounds - logoutRounds)
            return rounds

        if loginTime <= logoutTime:
            return calculateRounds(loginTime, logoutTime)
        else:
            return calculateRounds(loginTime, "24:00") + calculateRounds("00:00", logoutTime)


loginTime = "09:31"
logoutTime = "10:14"

loginTime = "21:30"
logoutTime = "03:00"

loginTime = "09:16"
logoutTime = "09:32"

loginTime = "00:01"
logoutTime = "00:00"

loginTime = "23:46"
logoutTime = "00:01"

loginTime = "00:47"
logoutTime = "00:57"

solution = Solution()
print(solution.numberOfRounds(loginTime, logoutTime))
