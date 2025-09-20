class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        s = "".join([ch.lower() for ch in s])

        # process
        ans = 0
        for x in range(1, L):
            if s[x] != s[x - 1]:
                ans += 1
        return ans


s = "aAbBcC"

solution = Solution()
print(solution.countKeyChanges(s))
