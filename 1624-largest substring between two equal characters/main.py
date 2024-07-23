class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(list)

        ans = -1
        for idx, ch in enumerate(s):
            dicts[ch].append(idx)
            if len(dicts[ch]) > 1:
                if dicts[ch][-1] - dicts[ch][0] > ans:
                    ans = dicts[ch][-1] - dicts[ch][0] - 1
        return ans


s = "aa"
s = "abca"
s = "cbzxy"

solution = Solution()
print(solution.maxLengthBetweenEqualCharacters(s))
