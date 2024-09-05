class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        # combination[0] - H8
        #            [1] - H4
        #            [2] - H2
        #            [3] - H1
        #            [4] - M32
        #            [5] - M16
        #            [6] - M8
        #            [7] - M4
        #            [8] - M2
        #            [9] - M1
        table = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def convertToTime(combination):
            hour = 0
            minute = 0
            for digit in combination:
                if digit < 4:
                    hour += table[digit]
                else:
                    minute += table[digit]

            if 0 <= hour < 12 and 0 <= minute < 60:
                if minute < 10:
                    return str(hour) + ":0" + str(minute)
                else:
                    return str(hour) + ":" + str(minute)
            return None

        import itertools
        ans = list()
        for combination in itertools.combinations(range(10), turnedOn):
            time = convertToTime(combination)
            if time:
                ans.append(time)
        return ans


turnedOn = 1
turnedOn = 9
turnedOn = 2

solution = Solution()
print(solution.readBinaryWatch(turnedOn))