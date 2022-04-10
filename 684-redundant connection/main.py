class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [x for x in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find_set = UnionFindSet(len(edges) + 1)
        for edge in edges:
            if not union_find_set.union(edge[0], edge[1]):
                return edge
        return []


solution = Solution()
edges = [[1, 2], [1, 3], [2, 3]]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

print(solution.findRedundantConnection(edges))
