class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process
        absents = 0
        consecutive_lates = 0
        for ch in s:
            if ch == "A":
                absents += 1
                if absents >= 2:
                    return False
            if ch == "L":
                consecutive_lates += 1
                if consecutive_lates >= 3:
                    return False
            else:
                consecutive_lates = 0
        return True


s = "PPALLP"
s = "PPALLL"
s = "PPLLAL"

solution = Solution()
print(solution.checkRecord(s))
