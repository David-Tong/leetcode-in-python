class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)

        # helper function
        def getCandidates(target):
            if target == 'a':
                return ('b', 'c')
            elif target == 'b':
                return ('a', 'c')
            else:
                return ('a', 'b')

        # helper function
        # get longest balanced string with only one ch
        def longestOne(target):
            res = 0
            count = 0
            for ch in s:
                if ch == target:
                    count += 1
                else:
                    res = max(res, count)
                    count = 0
            res = max(res, count)
            return res

        # helper function
        # get longest balanced string with only two chs
        def longestTwo(target):
            res = 0
            idx = 0
            start = -1
            while idx < L:
                if s[idx] == target:
                    end = idx
                    # process
                    res = max(res, searchTwo(target, start, end))
                    start = end
                idx += 1
            res = max(res, searchTwo(target, start, L))
            return res

        def searchTwo(target, start, end):
            res = 0
            ss = s[start + 1: end]
            candidates = getCandidates(target)
            from collections import defaultdict
            dicts = defaultdict(int)
            dicts[0] = -1
            presum = 0
            idx = 0
            while idx < len(ss):
                if ss[idx] == candidates[0]:
                    presum += 1
                elif ss[idx] == candidates[1]:
                    presum -= 1
                if presum in dicts:
                    res = max(res, idx - dicts[presum])
                else:
                    dicts[presum] = idx
                idx += 1
            return res

        # helper function
        # get longest balanced string with all three chs
        def longestThree():
            res = 0
            from collections import defaultdict
            dicts = defaultdict(int)
            dicts[(0, 0)] = -1
            # presum - difference between a and b
            # presum2 - difference between a and c
            # if the difference between a and b equals to the one between a and c
            # then a = b = c
            presum, presum2 = 0, 0
            idx = 0
            while idx < L:
                if s[idx] == 'a':
                    presum += 1
                    presum2 += 1
                elif s[idx] == 'b':
                    presum -= 1
                elif s[idx] == 'c':
                    presum2 -= 1
                if (presum, presum2) in dicts:
                    res = max(res, idx - dicts[(presum, presum2)])
                else:
                    dicts[(presum, presum2)] = idx
                idx += 1
            return res

        # process
        ans = 0
        for target in "abc":
            ans = max(ans, longestOne(target))
        for target in "abc":
            ans = max(ans, longestTwo(target))
        ans = max(ans, longestThree())
        return ans


s = "abbac"
s = "aabcc"
s = "aba"
s = "abcbc"

"""
import random
import string
s = "".join([random.choice("abc") for _ in range(10 ** 5)])
print(s)
"""

solution = Solution()
print(solution.longestBalanced(s))
