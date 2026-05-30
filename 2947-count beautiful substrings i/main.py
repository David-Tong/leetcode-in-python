import string


class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(s)
        vowels = [0]
        consonants = [0]
        idx = 0
        while idx < L:
            if s[idx] in "aeiou":
                vowels.append(vowels[-1] + 1)
                consonants.append(consonants[-1])
            else:
                vowels.append(vowels[-1])
                consonants.append(consonants[-1] + 1)
            idx += 1
        # print(vowels)
        # print(consonants)

        # process
        from collections import defaultdict
        dicts = defaultdict(set)
        dicts[0].add(0)

        count = 0
        idx = 0
        ans = 0
        while idx < L:
            if s[idx] in "aeiou":
                count += 1
            else:
                count -= 1

            for prev in dicts[count]:
                vowel = vowels[idx + 1] - vowels[prev]
                consonant = consonants[idx + 1] - consonants[prev]
                if vowel * consonant % k == 0:
                    ans += 1

            dicts[count].add(idx + 1)
            idx += 1

        return ans


s = "baeyh"
k = 2

s = "abba"
k = 1

s = "bcdf"
k = 1

import random
import string

s = "".join([random.choice(string.ascii_lowercase) for _ in range(1000)])
print(s)
k = 50

solution = Solution()
print(solution.beautifulSubstrings(s, k))
