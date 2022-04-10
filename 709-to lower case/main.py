class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for idx, ch in enumerate(s):
            if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
                ans += chr(ord(ch) + 32)
            else:
                ans += ch
        return ans


s = "Hello"
s = "here"
s = "LOVELY"
s = "a?AB-"

solution = Solution()
print(solution.toLowerCase(s))
