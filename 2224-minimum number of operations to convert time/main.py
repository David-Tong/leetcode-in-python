class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        # pre-process
        def convertToTime(input):
            hour, minute = input.split(":")
            return int(hour) * 60 + int(minute)

        current_time = convertToTime(current)
        correct_time = convertToTime(correct)

        # process
        delta = correct_time - current_time
        ans = 0
        for x in [60, 15, 5, 1]:
            ans += delta // x
            delta = delta % x
        return ans


current = "02:30"
correct = "04:35"

current = "11:00"
correct = "11:01"

current = "00:00"
correct = "23:48"

solution = Solution()
print(solution.convertTime(current, correct))
