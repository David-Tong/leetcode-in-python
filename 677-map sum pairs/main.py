class Trie(object):

    def __init__(self):
        self.nodes = {}
        self.value = 0

    def insert(self, word, value):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
            curr.value += value

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self
        try:
            for ch in word:
                curr = curr.nodes[ch]
        except:
            return 0

        return curr.value


class MapSum(object):

    def __init__(self):
        from collections import defaultdict
        self.words = defaultdict(int)
        self.trie = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key in self.words:
            delta = val - self.words[key]
            self.trie.insert(key, delta)
        else:
            self.trie.insert(key, val)
        self.words[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
ms = MapSum()
ms.insert("apple", 3)
print(ms.sum("ap"))
ms.insert("app", 2)
print(ms.sum("ap"))
