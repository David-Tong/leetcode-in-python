class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(word)
        VOWELS = "aeiou"
        from collections import defaultdict
        dicts = defaultdict(int)
        vowels = list()
        count = 0
        for x in range(L - 1, -1, -1):
            if word[x] in VOWELS:
                count += 1
            else:
                count = 0
            vowels.append(count)
        vowels = vowels[::-1]

        # process
        ans = 0
        # count - the number of vowels types
        # count2 - the number of consonants
        count, count2 = 0, 0
        # fast-slow two pointers
        y = 0
        # slow pointer
        for x in range(L):
            # fast pointer
            while y < L and (count < 5 or count2 < k):
                ch = word[y]
                if ch in VOWELS:
                    if dicts[ch] == 0:
                        count += 1
                    dicts[ch] += 1
                else:
                    count2 += 1
                y += 1

            # count == 5 and count2 >= k
            # case 1 : count == 5 and count2 == k
            # valid case
            if count == 5 and count2 == k:
                if y == L:
                    ans += 1
                else:
                    ans += 1 + vowels[y]

            # case 2 : count == 5 and count2 > k
            # invalid case

            ch = word[x]
            if ch in VOWELS:
                dicts[ch] -= 1
                if dicts[ch] == 0:
                    count -= 1
            else:
                count2 -= 1
        return ans


word = "aeioqq"
k = 1

word = "aeiou"
k = 0

"""
word = "ieaouqqieaouqq"
k = 1

word = "aeiouqaeiou"
k = 1

word = "ieaouqieaouq"
k = 1
"""

solution = Solution()
print(solution.countOfSubstrings(word, k))
