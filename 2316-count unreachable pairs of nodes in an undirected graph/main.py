class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(self.size)]
        self.ranks = [0] * self.size

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
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ufs = UnionFindSet(n)
        for edge in edges:
            ufs.union(edge[0], edge[1])
        for x in range(n):
            ufs.find(x)

        from collections import defaultdict
        groups = defaultdict(int)
        for parent in ufs.parents:
            groups[parent] += 1

        groups = groups.values()
        pairs = [0] * len(groups)
        for x in range(len(pairs) - 1, 0, -1):
            if x == len(pairs) - 1:
                pairs[x] = groups[-1]
            else:
                pairs[x] += groups[x] + pairs[x + 1]

        ans = 0
        for idx, group in enumerate(groups):
            if idx < len(groups) - 1:
                ans += group * pairs[idx + 1]
        return ans


n = 3
edges = [[0,1],[0,2],[1,2]]

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

n = 3
edges = []

solution = Solution()
print(solution.countPairs(n, edges))
