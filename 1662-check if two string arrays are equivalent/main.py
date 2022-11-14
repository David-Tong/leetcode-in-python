class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        def iterateArray(words):
            for word in words:
                for ch in word:
                    yield ch
            yield None

        g1 = iterateArray(word1)
        g2 = iterateArray(word2)
        while True:
            ch1 = next(g1)
            ch2 = next(g2)
            if ch1 is None and ch2 is None:
                return True
            if ch1 != ch2:
                return False


word1 = ["ab", "c"]
word2 = ["a", "bc"]

word1 = ["a", "cb"]
word2 = ["ab", "c"]

word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]

word1 = ["abc", "d", "defg", "h"]
word2 = ["abcddefg"]

solution = Solution()
print(solution.arrayStringsAreEqual(word1, word2))
