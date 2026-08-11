class LCATree:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.LOG = (n).bit_length()
        self.depths = [0] * (n + 1)
        self.ancestors = [[0] * self.LOG for _ in range(n + 1)]

        self._build()

    def _build(self):
        from collections import deque
        q = deque([1])
        self.depths[1] = 0
        self.ancestors[1][0] = 0

        visited = [False] * (self.n + 1)
        visited[1] = True

        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    self.depths[v] = self.depths[u] + 1
                    self.ancestors[v][0] = u
                    q.append(v)

        for k in range(1, self.LOG):
            for v in range(1, self.n + 1):
                mid = self.ancestors[v][k - 1]
                self.ancestors[v][k] = self.ancestors[mid][k - 1] if mid != 0 else 0

    def _lca(self, u, v):
        if self.depths[u] < self.depths[v]:
            u, v = v, u

        diff = self.depths[u] - self.depths[v]
        for k in range(self.LOG):
            if diff & (1 << k):
                u = self.ancestors[u][k]

        if u == v:
            return u

        for k in reversed(range(self.LOG)):
            if self.ancestors[u][k] != self.ancestors[v][k]:
                u = self.ancestors[u][k]
                v = self.ancestors[v][k]

        return self.ancestors[u][0]

    def distance(self, u, v):
        lca = self._lca(u, v)
        return self.depths[u] + self.depths[v] - 2 * self.depths[lca]


class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        N = len(edges) + 1
        MODULO = 10 ** 9 + 7
        lcaTree = LCATree(N, edges)

        # process
        ans = list()
        for u, v in queries:
            distance = lcaTree.distance(u, v)
            if distance == 0:
                ans.append(0)
            else:
                ans.append(pow(2, distance - 1, MODULO))
        return ans


edges = [[1,2]]
queries = [[1,1],[1,2]]

edges = [[1,2],[1,3],[3,4],[3,5]]
queries = [[1,4],[3,4],[2,5]]

solution = Solution()
print(solution.assignEdgeWeights(edges, queries))

