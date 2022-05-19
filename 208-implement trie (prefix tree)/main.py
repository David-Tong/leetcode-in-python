class Trie(object):

    def __init__(self):
        self.nodes = {}
        self.leaf = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.leaf = True

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
            return False

        return curr.leaf

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self
        try:
            for ch in prefix:
                curr = curr.nodes[ch]
        except:
            return False

        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
