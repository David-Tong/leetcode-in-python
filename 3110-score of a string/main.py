class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        ans = 0
        for x in range(L - 1):
            ans += abs(ord(s[x + 1]) - ord(s[x]))
        return ans


s = "hello"
s = "zaz"

solution = Solution()
print(solution.scoreOfString(s))
