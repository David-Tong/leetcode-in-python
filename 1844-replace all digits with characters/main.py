class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)

        ans = list(s)
        for x in range(0, L, 2):
            if x + 1 < L:
                ans[x + 1] = chr(ord(ans[x]) + int(ans[x + 1]))
        return "".join(ans)


s = "a1c1e1"
s = "a1b2c3d4e"

solution = Solution()
print(solution.replaceDigits(s))
