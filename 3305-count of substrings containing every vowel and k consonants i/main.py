class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(word)
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        CONSONANTS = 'c'
        from collections import defaultdict

        # helper functions
        def check(dicts):
            for vowel in VOWELS:
                if dicts[vowel] < 1:
                    return False
            if dicts[CONSONANTS] != k:
                return False
            return True

        def update(dicts, ch, operation):
            if ch in VOWELS:
                dicts[ch] += operation
            else:
                dicts[CONSONANTS] += operation

        # process
        # sliding window
        ans = 0
        for left in range(L):
            right = left
            dicts = defaultdict(int)
            while right < L and not check(dicts):
                ch = word[right]
                update(dicts, ch, 1)
                right += 1

            if check(dicts):
                ans += 1

            pivot = right
            while pivot < L and word[pivot] in VOWELS:
                pivot += 1
                ans += 1

            ch = word[left]
            update(dicts, ch, -1)
            left += 1
        return ans


word = "aeioqq"
k = 1

word = "aeiou"
k = 0

word = "ieaouqqieaouqq"
k = 1

solution = Solution()
print(solution.countOfSubstrings(word, k))
