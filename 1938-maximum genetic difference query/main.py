class Trie(object):
    def __init__(self):
        self.nodes = {}
        self.count = 0

    def insert(self, node):
        curr = self
        for x in range(31, -1, -1):
            d = (node >> x) & 1
            if d not in curr.nodes:
                curr.nodes[d] = Trie()
            curr = curr.nodes[d]
            curr.count += 1

    def query(self, val):
        curr = self
        res = 0
        for x in range(31, -1, -1):
            d = (val >> x) & 1
            if 1 - d in curr.nodes and curr.nodes[1 - d].count > 0:
                curr = curr.nodes[1 - d]
                res = res * 2 + 1 - d
            else:
                curr = curr.nodes[d]
                res = res * 2 + d
        return res

    def delete(self, node):
        curr = self
        for x in range(31, -1, -1):
            d = (node >> x) & 1
            curr = curr.nodes[d]
            curr.count -= 1


class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # there are three problems to solve
        # 1. how to pick up a from an array to maximize a ^ b
        #    using Trie
        # 2. how to solve queries when traversing the tree
        #    using DFS
        # 3. how to deal with backtracking when DFS for Trie
        #    for example, delete nodes in Trie
        #    by adding count attribute

        # pre-process
        from collections import defaultdict
        children = defaultdict(list)
        root = -1
        for idx, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(idx)
            else:
                root = idx

        Q = len(queries)
        qs = defaultdict(list)
        for idx, query in enumerate(queries):
            node, val = query
            qs[node].append((idx, val))

        # process
        ans = [0] * Q
        trie = Trie()

        # dfs
        def dfs(node):
            # update trie
            trie.insert(node)

            # update query
            for q in qs[node]:
                idx, val = q
                ans[idx] = val ^ trie.query(val)

            for child in children[node]:
                dfs(child)
                trie.delete(child)

        dfs(root)
        return ans


parents = [-1,0,1,1]
queries = [[0,2],[3,2],[2,5]]

parents = [3,7,-1,2,0,7,0,2]
queries = [[4,6],[1,15],[0,5]]

solution = Solution()
print(solution.maxGeneticDifference(parents, queries))