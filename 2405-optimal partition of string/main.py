class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        chs = defaultdict(bool)

        ans = 0
        for ch in s:
            if chs[ch]:
                ans += 1
                chs = defaultdict(bool)
            chs[ch] = True

        ans += 1
        return ans


s = "abacaba"
s = "ssssss"
s = "abcdefg"

solution = Solution()
print(solution.partitionString(s))
