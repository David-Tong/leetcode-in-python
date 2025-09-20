class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process
        flag = False
        for ch in s:
            if ch != "1":
                flag = True
            if flag:
                if ch == "1":
                    return False
        return True


s = "1001"
s = "110"

solution = Solution()
print(solution.checkOnesSegment(s))
