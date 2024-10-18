class Tier(object):
    def __init__(self):
        self.nodes = dict()
        self.counts = 0

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Tier()
            curr = curr.nodes[ch]
            curr.counts += 1

    def search(self, word):
        ans = 0
        curr = self
        try:
            for ch in word:
                curr = curr.nodes[ch]
                ans += curr.counts
        finally:
            return ans


class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        # pre-process
        trie = Tier()
        for word in words:
            trie.insert(word)

        # process
        ans = list()
        for word in words:
            ans.append(trie.search(word))
        return ans


words = ["abc","ab","bc","b"]
words = ["abcd"]
words = ["aaaaa","aaaa","aaa","aa","a","a"]

solution = Solution()
print(solution.sumPrefixScores(words))
