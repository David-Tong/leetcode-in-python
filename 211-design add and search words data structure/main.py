class WordDictionary(object):

    def __init__(self):
        self.words = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        length = len(word)
        if length not in self.words.keys():
            self.words[length] = set()
        self.words[length].add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        length = len(word)
        if length not in self.words.keys():
            return False

        if "." in word:
            return self.__search_with_dots(word)
        else:
            if word in self.words[length]:
                return True
            else:
                return False

    def __search_with_dots(self, word):
        length = len(word)
        for w in self.words[length]:
            i = 0
            while i < length:
                if word[i] == ".":
                    i += 1
                else:
                    if word[i] == w[i]:
                        i += 1
                    else:
                        break
            if i == length:
                return True
        return False


wordDictionary = WordDictionary()

wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");

print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))
