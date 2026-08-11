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
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        # short cut
        if len(edges) == 0:
            return 0

        # sort edges by weights
        edges.sort(key=lambda x: x[2])  # sort by weight

        # helper function
        def can(target):
            uf = UnionFindSet(n)

            # union edges with weight <= target
            for u, v, w in edges:
                if w > target:
                    break
                uf.union(u, v)

            # count components
            roots = set()
            for i in range(n):
                roots.add(uf.find(i))

            return len(roots) <= k

        # process
        # binary search
        left = 0
        right = max(w for _, _, w in edges)

        # binary search for minimum feasible target
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1

        if can(left):
            ans = left
        elif can(right):
            ans = right
        return ans


n = 5
edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]]
k = 2

n = 4
edges = [[0,1,5],[1,2,5],[2,3,5]]
k = 1

solution = Solution()
print(solution.minCost(n, edges, k))
