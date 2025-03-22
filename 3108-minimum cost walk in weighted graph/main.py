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
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict

        # build ufs
        ufs = UnionFindSet(n)
        for edge in edges:
            ufs.union(edge[0], edge[1])
        for x in range(n):
            ufs.find(x)

        # print(ufs.parents)

        # process costs
        costs = defaultdict(int)
        for edge in edges:
            parent = ufs.parents[edge[0]]
            if parent not in costs:
                costs[parent] = edge[2]
            else:
                costs[parent] &= edge[2]

        # process
        ans = list()
        for q in query:
            if ufs.parents[q[0]] == ufs.parents[q[1]]:
                ans.append(costs[ufs.parents[q[0]]])
            else:
                ans.append(-1)
        return ans


n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]

n = 3
edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
query = [[1,2]]

n = 7
edges = [[3,0,2],[5,4,12],[6,3,7],[4,2,2],[6,2,2]]
query = [[6,0]]

solution = Solution()
print(solution.minimumCost(n, edges, query))
