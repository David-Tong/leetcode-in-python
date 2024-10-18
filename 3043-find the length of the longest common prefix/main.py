class Trie(object):
    def __init__(self):
        self.nodes = dict()
        self.leaf = False

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = Trie()
            curr = curr.nodes[ch]
        curr.leaf = True

    def find(self, word):
        curr = self
        ans = 0
        try:
            for ch in word:
                curr = curr.nodes[ch]
                ans += 1
        finally:
            return ans


class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # pre-process
        trie = Trie()
        for num1 in arr1:
            trie.insert(str(num1))

        # process
        ans = 0
        for num2 in arr2:
            ans = max(ans, trie.find(str(num2)))
        return ans


arr1 = [1,10,100]
arr2 = [1000]

arr1 = [1,2,3]
arr2 = [4,4,4]

arr1 = [13,27,45]
arr2 = [21,27,48]

solution = Solution()
print(solution.longestCommonPrefix(arr1, arr2))
