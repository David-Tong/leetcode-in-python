class Trie(object):

    def __init__(self, label):
        self.label = label
        self.children = {}
        self.delete = False

    def insert(self, path):
        curr = self
        for p in path:
            if p not in curr.children:
                curr.children[p] = Trie(p)
            curr = curr.children[p]


class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        # pre-process
        # construct tree
        root = Trie('R')
        for path in paths:
            root.insert(path)
        # print(root)

        # search tag
        from collections import defaultdict
        tags = defaultdict(str)
        def tag(node):
            level, tg = 0, ""
            for c in sorted(node.children):
                child = node.children[c]
                level, _tg = tag(child)
                tg += str(level) + _tg
            tags[node] = tg
            return level + 1, node.label + tg

        tag(root)
        # print(tags)

        # process
        reversed_tags = defaultdict(int)
        for node in tags:
            reversed_tags[tags[node]] += 1

        nodes_to_delete = list()
        for node in tags:
            if tags[node] != "":
                if reversed_tags[tags[node]] > 1:
                    nodes_to_delete.append(node)
        # print(nodes_to_delete)

        # delete nodes
        from collections import deque
        bfs = deque()
        bfs.append(root)
        while bfs:
            curr = bfs.popleft()
            for c in curr.children:
                child = curr.children[c]
                if child in nodes_to_delete:
                    child.delete = True
                else:
                    bfs.append(child)
        # print(root)

        # post-proces
        ans = list()
        def collect(node, path):
            if node != root:
                ans.append(path + [node.label])
            for c in node.children:
                child = node.children[c]
                if not child.delete:
                    if node == root:
                        collect(child, path)
                    else:
                        collect(child, path + [node.label])
        collect(root, list())
        # print(ans)
        return ans


paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
paths = [["a","b"],["c","d"],["c"],["a"]]
paths = [["b"],["f"],["f","r"],["f","r","g"],["f","r","g","c"],["f","r","g","c","r"],["f","o"],["f","o","x"],["f","o","x","t"],["f","o","x","d"],["f","o","l"],["l"],["l","q"],["c"],["h"],["h","t"],["h","o"],["h","o","d"],["h","o","t"]]
paths = [["a"],["a","c"],["a","d"],["a","d","e"],["b"],["b","e"],["b","c"],["b","c","d"],["f"],["f","h"],["f","h","i"],["f","j"],["g"],["g","j"],["g","h"],["g","h","i"]]

solution = Solution()
print(solution.deleteDuplicateFolder(paths))
