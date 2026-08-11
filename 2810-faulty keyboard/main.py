class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # process
        ans = ""
        for ch in s:
            if ch == "i":
                ans = ans[::-1]
            else:
                ans += ch
        return ans


s = "string"
s = "poiinter"


solution = Solution()
print(solution.finalString(s))
