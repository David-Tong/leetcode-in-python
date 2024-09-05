class UnionFindSet(object):
    def __init__(self, N):
        from collections import defaultdict
        self.N = N
        self.parents = [_ for _ in range(N)]
        self.ranks = [0] * N

    def find(self, x):
        if self.parents[x] != x:
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
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        edges = zip(edges, [_ for _ in range(len(edges))])
        edges = sorted(edges, key=lambda x:x[0][2])

        # MST
        def mst(include, exclude):
            ufs = UnionFindSet(n)
            count = 0
            cost = 0
            if include is not None:
                ufs.union(include[0][0], include[0][1])
                count += 1
                cost += include[0][2]
            for edge in edges:
                if exclude is not None and edge[1] == exclude[1]:
                    continue
                else:
                    if ufs.union(edge[0][0], edge[0][1]):
                        count += 1
                        cost += edge[0][2]
            if count == n - 1:
                return cost
            else:
                return float("inf")

        baseline = mst(None, None)

        criticals = list()
        pseudos = list()
        for edge in edges:
            if mst(None, edge) > baseline:
                criticals.append(edge[1])
            elif mst(edge, None) == baseline:
                pseudos.append(edge[1])
        return [criticals, pseudos]


n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

n = 4
edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]

solution = Solution()
print(solution.findCriticalAndPseudoCriticalEdges(n, edges))
