class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        # process
        min_even, maxi_odd = float("inf"), 0
        for ch in dicts:
            if dicts[ch] % 2 == 0:
                min_even = min(min_even, dicts[ch])
            else:
                maxi_odd = max(maxi_odd, dicts[ch])
        ans = maxi_odd - min_even
        return ans


s = "aaaaabbc"
s = "abcabcab"

solution = Solution()
print(solution.maxDifference(s))
