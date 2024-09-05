class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [x for x in range(self.size)]
        self.ranks = [0] * self.size

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
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        L = len(vals)
        conns = edges

        from collections import defaultdict
        vertices = defaultdict(list)
        edges = defaultdict(list)

        for idx, val in enumerate(vals):
            vertices[val].append(idx)

        for conn in conns:
            key = max(vals[conn[0]], vals[conn[1]])
            edges[key].append(conn)

        ufs = UnionFindSet(L)
        ans = 0
        for val in sorted(vertices.keys()):
            for edge in edges[val]:
                ufs.union(edge[0], edge[1])
            for vertex in vertices[val]:
                ufs.find(vertex)

            forest = defaultdict(int)
            for vertex in vertices[val]:
                key = ufs.parents[vertex]
                forest[key] += 1

            # count
            for key, value in forest.items():
                if value == 1:
                    ans += 1
                elif value > 1:
                    ans = ans + value + (value * (value - 1 )) // 2
        return ans


vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]

vals = [1,1,2,2,3]
edges = [[0,1],[1,2],[2,3],[2,4]]

vals = [1]
edges = []

solution = Solution()
print(solution.numberOfGoodPaths(vals, edges))
