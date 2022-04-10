class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s) - 1
        fast = N
        slow = -1
        while fast >= 0:
            if s[fast] == " ":
                if slow != -1:
                    return slow - fast
            else:
                if slow == -1:
                    slow = fast
            fast -= 1
        return slow - fast


s = "Hello World"
s = "   fly me   to   the moon  "
s = "joyboy"
s = "  joyboy"
s = "1"

solution = Solution()
print(solution.lengthOfLastWord(s))
