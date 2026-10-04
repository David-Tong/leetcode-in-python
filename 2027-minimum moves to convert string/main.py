class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # process
        ans = 0
        idx = 0
        while idx < L:
            if s[idx] == "X":
               ans += 1
               idx += 2
            idx += 1
        return ans


s = "XXX"
s = "XXOX"

solution = Solution()
print(solution.minimumMoves(s))
