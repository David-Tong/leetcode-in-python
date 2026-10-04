class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        def getReversedIndex(ch):
            return ord('z') - ord(ch) + 1

        # process
        ans = 0
        idx = 0
        while idx < L:
            ans += getReversedIndex(s[idx]) * (idx + 1)
            idx += 1
        return ans


s = "abc"
s = "zaza"

solution = Solution()
print(solution.reverseDegree(s))
