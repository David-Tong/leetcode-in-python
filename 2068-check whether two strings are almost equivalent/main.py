class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch1 in word1:
            dicts[ch1] += 1
        for ch2 in word2:
            dicts[ch2] -= 1

        # process
        for ch in dicts:
            if abs(dicts[ch]) > 3:
                return False
        return True


word1 = "aaaa"
word2 = "bccb"

word1 = "abcdeef"
word2 = "abaaacc"

word1 = "cccddabba"
word2 = "babababab"

solution = Solution()
print(solution.checkAlmostEquivalent(word1, word2))
