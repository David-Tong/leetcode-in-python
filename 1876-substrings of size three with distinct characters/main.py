class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        ans = 0
        for idx, ch in enumerate(s):
            if idx < 3:
                dicts[ch] += 1
            else:
                prev = s[idx - 3]
                dicts[ch] += 1
                dicts[prev] -= 1
                if dicts[prev] == 0:
                    del dicts[prev]
            if len(dicts) == 3:
                ans += 1
        return ans


s = "xyzzaz"
s = "aababcabc"

solution = Solution()
print(solution.countGoodSubstrings(s))
