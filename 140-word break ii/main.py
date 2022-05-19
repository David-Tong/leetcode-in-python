class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        dicts = defaultdict(list)
        self.L = 0
        for word in wordDict:
            dicts[len(word)].append(word)
            self.L = max(self.L, len(word))

        self.anses = []
        def doBreak(s, words, dicts):
            if len(s) == 0:
                self.anses.append(" ".join(words))
            else:
                for x in range(self.L):
                    if x < len(s):
                        word = s[:x+1]
                        if word in dicts[len(word)]:
                            doBreak(s[x+1:], words + [word], dicts)

        doBreak(s, [], dicts)
        return self.anses


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

solution = Solution()
print(solution.wordBreak(s, wordDict))
