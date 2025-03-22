class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        ans = 0
        for x in range(0, L, 2):
            if s[x] != s[x + 1]:
                ans += 1
        return ans


s = "1001"
s = "10"
s = "0000"

solution = Solution()
print(solution.minChanges(s))
