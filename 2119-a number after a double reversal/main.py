class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # pre-process
        if num == 0:
            return True

        # process
        num = str(num)
        return num[-1] != "0"


num = 526
num = 1800
num = 0

solution = Solution()
print(solution.isSameAfterReversals(num))
