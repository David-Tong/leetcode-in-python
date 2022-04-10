class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        index2 = 0
        while index < len(s) and index2 < len(t):
            if s[index] == t[index2]:
                index += 1
            index2 += 1

        if index == len(s):
            return True
        else:
            return False


s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"

s = ""
t = "aaa"

s = "acb"
t = "ahbgdc"

solution = Solution()
print(solution.isSubsequence(s, t))
