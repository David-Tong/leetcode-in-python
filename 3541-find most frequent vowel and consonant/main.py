class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s:
            dicts[ch] += 1

        # process
        VOWELS = "aeiou"
        vowel, consonant = 0, 0
        for ch in dicts:
            if ch in VOWELS:
                vowel = max(vowel, dicts[ch])
            else:
                consonant = max(consonant, dicts[ch])
        ans = vowel + consonant
        return ans


s = "successes"
s = "aeiaeia"

solution = Solution()
print(solution.maxFreqSum(s))
