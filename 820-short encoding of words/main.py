class Trie(object):

    def __init__(self):
        self.nodes = dict()

    def insert(self, words):
        curr = self
        for ch in words:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])

        self.ans = 0
        def doSearch(curr, depth):
            if len(curr.parents) == 0:
                self.ans += depth
                return

            for key in curr.parents:
                doSearch(curr.parents[key], depth + 1)

        doSearch(trie, 1)
        return self.ans


words = ["time", "me", "bell"]
words = ["t"]
words = ["time", "ti", "me"]

solution = Solution()
print(solution.minimumLengthEncoding(words))
