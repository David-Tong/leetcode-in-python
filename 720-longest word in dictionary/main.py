class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.leaf = False

    def insert(self, word):
        valid = True
        curr = self
        for idx, ch in enumerate(word):
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            if idx < len(word):
                valid &= curr.leaf
            curr = curr.nodes[ch]
        curr.leaf = True
        return valid


class Solution(object):
    def __init__(self):
        self.trie = Trie()
        self.trie.leaf = True

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        longest = 0
        ans = ""
        for word in words:
            if self.trie.insert(word):
                if len(word) > longest:
                    longest = len(word)
                    ans = word
        self.trie
        return ans


words = ["w","wo","wor","worl","world"]
words = ["a","banana","app","appl","ap","apply","apple"]
words = ["a"]
words = ["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"]


solution = Solution()
print(solution.longestWord(words))
