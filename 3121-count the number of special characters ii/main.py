class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        from string import ascii_lowercase, ascii_uppercase
        for idx, ch in enumerate(word):
            if ch in ascii_lowercase:
                dicts[ch] = idx
            elif ch in ascii_uppercase:
                if ch not in dicts:
                    dicts[ch] = idx

        # process

        ans = 0
        for key in dicts:
            if key in ascii_lowercase:
                upper = key.upper()
                if upper in dicts.keys():
                    if dicts[key] < dicts[upper]:
                        ans += 1
        return ans


word = "aaAbcBC"
word = "abc"
word = "AbBCab"

import random
from string import ascii_letters
word = "".join(random.choice(ascii_letters) for _ in range(2 * 10 ** 5))
print(word)

solution = Solution()
print(solution.numberOfSpecialChars(word))
