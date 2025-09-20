class MagicDictionary(object):

    def __init__(self):
        pass

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.dictionary = dictionary

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        L = len(searchWord)
        for word in self.dictionary:
            if len(word) == L:
                idx = 0
                unmatched = 0
                while idx < L:
                    if word[idx] != searchWord[idx]:
                        unmatched += 1
                        if unmatched > 1:
                            break
                    idx += 1
                if unmatched == 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

dictionary = ["hello", "leetcode"]

md = MagicDictionary()
md.buildDict(dictionary)
print(md.search("hello"))
print(md.search("hhllo"))
print(md.search("hell"))
print(md.search("leetcoded"))
