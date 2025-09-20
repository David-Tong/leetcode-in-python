class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(s)
        from collections import defaultdict
        ranges = defaultdict(list)
        for x in range(L):
            if s[x] not in ranges:
                ranges[s[x]].append(x)
        for x in range(L - 1, -1, -1):
            if len(ranges[s[x]]) == 1:
                ranges[s[x]].append(x)
        # print(ranges)

        # count valid intervals
        intervals = list()
        for ch in ranges:
            start, end = ranges[ch]
            x = start + 1
            valid = True
            while x < end:
                if ranges[s[x]][0] < start:
                    valid = False
                    break
                end = max(end, ranges[s[x]][1])
                x += 1

            if valid:
                if start == 0 and end == L - 1:
                    continue
                else:
                    intervals.append((start, end))

        # print(intervals)

        # process
        if intervals:
            intervals = sorted(intervals, key=lambda x: x[1])
            count = 1
            limit = intervals[0][1]
            for interval in intervals[1:]:
                start, end = interval
                if start > limit:
                    count += 1
                    limit = end

            ans = count >= k
            return ans
        else:
            return k == 0


s = "abcdbaefab"
k = 2

s = "cdefdc"
k = 3

s = "abeabe"
k = 0

s = "nbuirvanjiccnsyyyoirleqsrwrvxepaglcidqplyryujytzqoncxjgwdmatytgwhzyhlsodrbzrpbbitovtdasazjtoyyfhowqqrzuvjveydceouscrfazzoblqhalhfybwheybkpcroijxvarrtqrqnmwslkpdducfeblvfecyjyulxgahxlzlyztssfzwvfujrriryslkvdwhmkcyebfhkadrahunvxivkwitilyzknwyujtylahgmlddymlbrbrniomepbmdieasuvdcqnzfwspxewbbpruxrznjxwnjjxvblxyrgv"
k = 1

s ="cbcaba"
k = 1

s = "acdbdbca"
k = 1

s = "cbcaba"
k = 1

"""
import random
import string
s = "".join([random.choice(string.ascii_lowercase) for _ in range(150)])
k = 10
print(s)
"""

solution = Solution()
print(solution.maxSubstringLength(s, k))
