class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        # pre-process
        L = len(target)

        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1
        keys = sorted(dicts.keys())
        K = len(keys)

        # helper function
        # find the existing character greater than ch
        def greater(ch):
            idx = 0
            while idx < K:
                key = keys[idx]
                if key > ch:
                    if dicts[key] > 0:
                        return key
                idx += 1
            return None

        # make the string in a lexicographically smallest way'
        def compose():
            res = ""
            for key in keys:
                if dicts[key] > 0:
                    res += key * dicts[key]
            return res

        # find the next greater permutation
        def advance(s):
            res = list(s)
            idx = L - 1
            while idx > 0 and s[idx - 1] >= s[idx]:
                idx -= 1
            if idx > 0:
                idx -= 1
                idx2 = L - 1
                while idx2 > idx and s[idx2] <= s[idx]:
                    idx2 -= 1
                res[idx2], res[idx] = res[idx], res[idx2]
                res[idx + 1:] = reversed(res[idx + 1:])
                res = "".join(res)
            else:
                res = ""
            return res

        # process
        idx = 0
        while idx < L:
            ch = target[idx]
            if dicts[ch] > 0:
                dicts[ch] -= 1
            else:
                break
            idx += 1

        # if s == target
        if idx == L:
            ans = advance(target)
        # else
        else:
            ans = ""
            back = False
            while idx >= 0:
                ch = target[idx]
                candidate = greater(ch)
                if candidate is not None:
                    if back:
                        dicts[ch] += 1
                    dicts[candidate] -= 1
                    ans = target[:idx] + candidate + compose()
                    break
                if not back:
                    back = True
                else:
                    ch2 = target[idx]
                    dicts[ch2] += 1
                idx -= 1
        return ans


s = "abc"
target = "bba"

"""
s = "leet"
target = "code"

s = "baba"
target = "bbaa"

s = "b"
target = "b"

s = "b"
target = "c"

s = "b"
target = "a"

s = "ab"
target = "ab"

s = "ba"
target = "ab"

s = "aab"
target = "aab"

s = "aab"
target = "aba"

s = "aab"
target = "abb"

s = "aab"
target = "bab"
"""

s = "abb"
target = "abb"

"""
from random import choice
from string import ascii_lowercase
s = "".join(choice(ascii_lowercase) for _ in range(300))
target = "".join(choice(ascii_lowercase) for _ in range(300))
print(s)
print(target)
"""

solution = Solution()
print(solution.lexGreaterPermutation(s, target))
