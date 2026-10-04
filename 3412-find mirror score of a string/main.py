class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        L = len(s)
        from collections import defaultdict

        # helper function
        def getMirror(c):
            return chr(ord('a') + ord('z') - ord(c))

        # process
        dicts = defaultdict(list)
        ans = 0
        idx = 0
        while idx < L:
            ch = s[idx]
            mirror = getMirror(ch)

            if dicts[mirror]:
                idx2 = dicts[mirror].pop()
                ans += idx - idx2
            else:
                dicts[ch].append(idx)
            idx += 1
        return ans


s = "aczzx"
s = "abcdef"

from random import choice
from string import ascii_lowercase
s = "".join(choice(ascii_lowercase) for _ in range(10 ** 5))
print(s)

solution = Solution()
print(solution.calculateScore(s))
