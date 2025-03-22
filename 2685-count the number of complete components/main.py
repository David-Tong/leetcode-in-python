class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.ranks[px] > self.ranks[py]:
                self.parents[py] = px
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True


class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        ufs = UnionFindSet(n)
        for edge in edges:
            ufs.union(edge[0], edge[1])
        for x in range(n):
            ufs.find(x)

        from collections import defaultdict
        vertices = defaultdict(int)
        for x in range(n):
            vertices[ufs.parents[x]] += 1

        # process
        paths = defaultdict(int)
        for edge in edges:
            paths[ufs.parents[edge[0]]] += 1

        # post-process
        ans = 0
        for vertex in vertices:
            if paths[vertex] == vertices[vertex] * (vertices[vertex] - 1) // 2:
                ans += 1
        return ans


n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]

n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]

n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5],[4,5]]

solution = Solution()
print(solution.countCompleteComponents(n, edges))
