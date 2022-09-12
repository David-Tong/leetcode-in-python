class Trie(object):

    def __init__(self):
        self.nodes = dict()
        self.indexes = set()

    def insert(self, idx, word):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr.nodes[ch].indexes.add(idx)
            curr = curr.nodes[ch]

    def startsWith(self, prefix):
        curr = self
        try:
            for ch in prefix:
                curr = curr.nodes[ch]
        except:
            return set()

        return curr.indexes


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.cache = {}

        for idx, word in enumerate(words):
            reversed_word = word[::-1]
            self.prefix_trie.insert(idx, word)
            self.suffix_trie.insert(idx, reversed_word)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        if prefix in self.cache and suffix in self.cache[prefix]:
            return self.cache[prefix][suffix]
        else:
            self.cache[prefix] = {}
            self.cache[prefix][suffix] = -1

        prefix_idxes = self.prefix_trie.startsWith(prefix)
        suffix_idxes = self.suffix_trie.startsWith(suffix[::-1])

        for prefix_idx in sorted(prefix_idxes, reverse=True):
            if prefix_idx in suffix_idxes:
                self.cache[prefix][suffix] = prefix_idx
                return prefix_idx

        return -1


"""
words = ["apple", "banana", "bagna"]
wf = WordFilter(words)
print(wf.f("b", "na"))
"""

words = ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
wf = WordFilter(words)
print(wf.f("bccbacbcba","a"))
print(wf.f("ab","abcaccbcaa"))
print(wf.f("a","aa"))
print(wf.f("cabaaba","abaaaa"))
print(wf.f("cacc","accbbcbab"))
print(wf.f("ccbcab","bac"))
print(wf.f("bac","cba"))
print(wf.f("ac","accabaccaa"))
print(wf.f("bcbb","aa"))
print(wf.f("ccbca","cbcababac"))
