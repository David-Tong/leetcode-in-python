class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        dicts = defaultdict(int)

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for idx, row in enumerate(rows):
            for ch in row:
                dicts[ch] = idx

        ans = list()
        for word in words:
            from string import lower
            lower_word = lower(word)
            base = dicts[lower_word[0]]
            one_row = True
            for ch in lower_word:
                if dicts[ch] != base:
                    one_row = False
                    break
            if one_row:
                ans.append(word)
        return ans


words = ["Hello","Alaska","Dad","Peace"]
words = ["omk"]
words = ["adsdf","sfd"]

solution = Solution()
print(solution.findWords(words))
