class Trie(object):

    def __init__(self):
        self.limit = 3
        self.nodes = dict()
        self.indexes = list()

    def insert(self, idx, word):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr.nodes[ch].indexes.append(idx)
            curr = curr.nodes[ch]

    def search(self, prefix):
        curr = self
        try:
            for ch in prefix:
                curr = curr.nodes[ch]
        except:
            return list()
        return curr.indexes[:self.limit]


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products = sorted(products)
        trie = Trie()
        for idx, product in enumerate(products):
            trie.insert(idx, product)

        anses = list()
        L = len(searchWord)
        for idx in range(L):
            ans = list()
            indexes = trie.search(searchWord[:idx + 1])
            for index in indexes:
                ans.append(products[index])
            anses.append(ans)
        return anses


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

products = ["havana"]
searchWord = "havana"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

solution = Solution()
print(solution.suggestedProducts(products, searchWord))
