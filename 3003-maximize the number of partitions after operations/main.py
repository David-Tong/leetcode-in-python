class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)

        # process
        from collections import defaultdict
        cache = defaultdict(int)
        # dfs
        # idx - the s[idx] being processed
        # mask - the mask for processed prefix
        # changed - whether the change has been made
        def dfs(idx, mask, changed):
            key = "{}-{}-{}".format(idx, mask, changed)
            if key in cache:
                return cache[key]

            if idx == L:
                return 1

            # process s[idx]
            bit = 1 << (ord(s[idx]) - ord('a'))
            new_mask = mask | bit
            # have to split
            if bin(new_mask).count('1') > k:
                res = dfs(idx + 1, bit, changed) + 1
            else:
                res = dfs(idx + 1, new_mask, changed)

            # not change s[idx]
            if changed:
                cache[key] = res
                return res

            # change s[idx]
            for x in range(26):
                bit = 1 << x
                new_mask = mask | bit
                if bin(new_mask).count('1') > k:
                    # have to split
                    res = max(res, dfs(idx + 1, bit, True) + 1)
                else:
                    res = max(res, dfs(idx + 1, new_mask, True))
            cache[key] = res
            return res

        return dfs(0, 0, False)


s = "accca"
k = 2

s = "aabaab"
k = 3

s = "xxyz"
k = 1

import sys
sys.setrecursionlimit(10 ** 4)
import random
import string
s = "".join([random.choice(string.ascii_lowercase) for _ in range(10 ** 3)])
print(s)
k = 20

solution = Solution()
print(solution.maxPartitionsAfterOperations(s, k))
