class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        from collections import defaultdict
        keys = set()
        for ch in s:
            keys.add(ch)

        dicts = defaultdict(list)
        for key in keys:
            dicts[key].append(0)

        for ch in s:
            for key in keys:
                if ch == key:
                    dicts[key].append(dicts[key][-1] + 1)
                else:
                    dicts[key].append(dicts[key][-1])

        # print(dicts)

        # helper function
        def valid(start, end):
            target = 0
            for key in keys:
                diff = dicts[key][end + 1] - dicts[key][start]
                if diff > 0:
                    if target > 0:
                        if diff != target:
                            return False
                    else:
                        target = diff
            return True

        # process
        step = L - 1
        while step > 0:
            start = 0
            end = start + step
            while end < L:
                if valid(start, end):
                    return step + 1
                start += 1
                end += 1
            step -= 1
        return 1


s = "abbac"
# s = "zzabccy"
# s = "aba"

"""
import random
import string
s = "".join([random.choice(string.ascii_lowercase) for _ in range(10 ** 3)])
print(s)
"""

solution = Solution()
print(solution.longestBalanced(s))
