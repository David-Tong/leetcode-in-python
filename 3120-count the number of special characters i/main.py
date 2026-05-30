class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)

        for idx, ch in enumerate(word):
            if ch not in dicts:
                dicts[ch] = idx

        # process
        from string import ascii_lowercase
        ans = 0
        for key in dicts:
            if key in  ascii_lowercase:
                upper = key.upper()
                if upper in dicts.keys():
                    ans += 1
        return ans


word = "aaAbcBC"
word = "abc"
word = "abBCab"

solution = Solution()
print(solution.numberOfSpecialChars(word))
