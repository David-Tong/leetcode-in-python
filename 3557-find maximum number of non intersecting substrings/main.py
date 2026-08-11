class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        L = 4

        # process
        from collections import defaultdict
        dicts = defaultdict(int)

        ans = 0
        for idx, ch in enumerate(word):
            if ch not in dicts:
                dicts[ch] = idx
            else:
                if idx - dicts[ch] >= L - 1:
                    dicts = defaultdict(int)
                    ans += 1
        return ans


word = "abcdeafdef"
word = "bcdaaaab"

from string import ascii_lowercase
from random import choice
word = "".join([choice(ascii_lowercase) for _ in range(2 * 10 ** 5)])
print(word)

solution = Solution()
print(solution.maxSubstrings(word))
