class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        self.ans = 0

        def doLongestSubString(s, k):
            from collections import defaultdict
            dicts = defaultdict(int)

            for ch in s:
                dicts[ch] += 1

            outs = list()
            for ch in dicts:
                if dicts[ch] < k and dicts[ch] != 0:
                    outs.append(ch)

            if len(outs) == 0:
                self.ans = max(self.ans, len(s))
                return

            prev = 0
            subs = list()
            for idx, ch in enumerate(s):
                if ch in outs:
                    if idx - prev >= k:
                        subs.append(s[prev:idx])
                    prev = idx + 1
            subs.append(s[prev:])

            for sub in subs:
                doLongestSubString(sub, k)

        doLongestSubString(s, k)
        return self.ans


s = "aaabb"
k = 3

"""
s = "ababbc"
k = 2

s = "abbba"
k = 3

s = "bbaaab"
k = 3

s = "a"
k = 1

s = "a"
k = 2

s = "ababacb"
k = 3

s = "bbaaacbd"
k = 3
"""

solution = Solution()
print(solution.longestSubstring(s, k))
