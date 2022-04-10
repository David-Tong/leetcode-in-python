class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        from collections import defaultdict
        self.dicts = defaultdict(chr)
        for idx, ch in enumerate(order):
            self.dicts[ch] = idx

        from functools import cmp_to_key
        def compare(word, word2):
            idx = 0
            idx2 = 0
            while idx < len(word) and idx2 < len(word2):
                if self.dicts[word[idx]] < self.dicts[word2[idx]]:
                    return -1
                elif self.dicts[word[idx]] > self.dicts[word2[idx]]:
                    return 1
                else:
                    idx += 1
                    idx2 += 1

            if idx < len(word):
                return 1
            if idx2 < len(word2):
                return -1
            return 0

        sorted_words = sorted(words, key=cmp_to_key(compare))
        for x in range(len(words)):
            if sorted_words[x] != words[x]:
                return False
        return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

words = ["bb", "b", "a"]
order = "ba"

solution = Solution()
print(solution.isAlienSorted(words, order))
