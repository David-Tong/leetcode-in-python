class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num + 2 * t


num = 4
t = 1

solution = Solution()
print(solution.theMaximumAchievableX(num, t))
