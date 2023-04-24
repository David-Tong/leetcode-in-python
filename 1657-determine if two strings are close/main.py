class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        def countFrequency(word):
            from collections import defaultdict
            dicts = defaultdict(int)
            for ch in word:
                dicts[ch] += 1

            frequency = defaultdict(int)
            for k, v in dicts.items():
                frequency[v] += 1

            return frequency

        frequency = countFrequency(word1)
        frequency2 = countFrequency(word2)

        if set(word1) != set(word2):
            return False

        for f in frequency:
            if f in frequency2:
                if frequency[f] != frequency2[f]:
                    return False
            else:
                return False

        return True


word1 = "abc"
word2 = "bca"

word1 = "a"
word2 = "aa"

word1 = "cabbba"
word2 = "abbccc"

word1 = "cabcbc"
word2 = "caabbb"

solution = Solution()
print(solution.closeStrings(word1, word2))
