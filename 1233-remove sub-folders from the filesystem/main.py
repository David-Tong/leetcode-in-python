class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.leaf = False

    def insert(self, paths):
        """
        :type word: str
        :rtype: None
        """
        curr = self
        parent = None
        for path in paths:
            if curr.leaf:
                return False
            if path not in curr.nodes:
                curr.nodes[path] = Trie()
            curr = curr.nodes[path]
        curr.leaf = True
        return True


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # pre-process
        folder = sorted(folder)
        trie = Trie()

        # process
        ans = list()
        for fld in folder:
            paths = fld.split("/")[1:]
            if trie.insert(paths):
                ans.append(fld)
        return ans


folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
folder = ["/a","/a/b/c","/a/b/d"]
folder = ["/a/b/c","/a/b/ca","/a/b/d"]

solution = Solution()
print(solution.removeSubfolders(folder))
