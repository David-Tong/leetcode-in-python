class Trie(object):
    def __init__(self):
        self.nodes = {}
        # record the earliest/best index reaching this node
        self.idx = None
        self.leaf = False

    def insert(self, word, idx):
        curr = self
        if curr.idx is None:
            curr.idx = idx

        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]

            # only set idx the first time this node is visited
            if curr.idx is None:
                curr.idx = idx
        curr.leaf = True


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        # pre-process
        # sort wordsContainer by (length, original index)
        indexed = [(len(w), i, w) for i, w in enumerate(wordsContainer)]
        indexed.sort()  # Python sorts tuples lexicographically

        # build reversed Trie
        root = Trie()
        for _, orig_idx, word in indexed:
            rev = word[::-1]
            root.insert(rev, orig_idx)

        # process
        # search each query
        ans = []
        for query in wordsQuery:
            curr = root
            # root.idx should be the shortest word overall
            best = curr.idx
            for ch in reversed(query):
                if ch not in curr.nodes:
                    break
                curr = curr.nodes[ch]
                # deeper node and longer suffix match
                best = curr.idx
            ans.append(best)

        return ans


wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]

wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
wordsQuery = ["gh","acbfgh","acbfegh"]

import random
import string
wordsContainer = [''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(10 ** 3)]
wordsQuery = [''.join(random.choice(string.ascii_lowercase) for _ in range(5)) for _ in range(10 ** 3)]

print(wordsContainer)
print(wordsQuery)

solution = Solution()
print(solution.stringIndices(wordsContainer, wordsQuery))
