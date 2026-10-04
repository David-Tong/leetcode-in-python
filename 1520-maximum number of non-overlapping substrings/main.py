class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # pre-process
        from collections import defaultdict

        # find the first and the last occurrence of each character
        first = defaultdict(lambda: float('inf'))
        last = defaultdict(lambda: -1)
        for idx, ch in enumerate(s):
            first[ch] = min(first[ch], idx)
            last[ch] = max(last[ch], idx)

        # process s and find every substring match condition 2
        # substring that contains a certain character c must also contain all occurrences of c.
        intervals = set()
        for ch in first:
            left = int(first[ch])
            right = int(last[ch])

            expanded = True
            while expanded:
                expanded = False
                idx = left
                while idx <= right:
                    ch2 = s[idx]
                    if first[ch2] < left:
                        left = first[ch2]
                        expanded = True
                    if last[ch2] > right:
                        right = last[ch2]
                        expanded = True
                    idx += 1
            intervals.add((left, right))

        # process
        # use greedy algorithm to find maximum number non-overlapping intervals
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        ans = list()
        limit = -1
        for left, right in intervals:
            if left > limit:
                ans.append(s[left:right + 1])
                limit = right
        return ans


s = "adefaddaccc"
s = "abbaccd"

from random import choice
import string
s = "".join([choice(string.ascii_lowercase) for _ in range(10 ** 5)])
print(s)

solution = Solution()
print(solution.maxNumOfSubstrings(s))
