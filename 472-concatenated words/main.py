class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.dicts = set()
        for word in words:
            self.dicts.add(word)

        from collections import defaultdict
        self.concatenations = defaultdict(int)

        anses = list()
        for word in words:
            if word in self.concatenations:
                anses.append(word)
            else:
                res, _ = self.__do_find(word, 0)
                if res:
                    anses.append(word)
        return anses

    def __do_find(self, word, concatenation):
        if len(word) == 0:
            if concatenation >= 2:
                return True, concatenation
            else:
                return False, None

        for x in range(1, len(word) + 1):
            if word[:x] in self.dicts:
                if word[x:] in self.concatenations:
                    return True, concatenation + self.concatenations[word[x:]]
                else:
                    res, final = self.__do_find(word[x:], concatenation + 1)
                    if res:
                        if final - concatenation > 1:
                            self.concatenations[word] = final - concatenation
                        return True, final
        return False, None


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["cat","dog","catdog"]

solution = Solution()
print(solution.findAllConcatenatedWordsInADict(words))
