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
    def minTime(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(edges)
        edges = sorted(edges, key=lambda edge: edge[2])

        # process
        # check function
        def can(target):
            ufs = UnionFindSet(n)
            for edge in edges[target:]:
                ufs.union(edge[0], edge[1])
            for vertex in range(n):
                ufs.find(vertex)
            components = set()
            for vertex in range(n):
                components.add(ufs.parents[vertex])
            return len(components) >= k

        # binary search
        left, right = 0, L
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1
        if can(left):
            if left == 0:
                return 0
            else:
                return edges[left - 1][2]
        elif can(right):
            return edges[right - 1][2]


n = 2
edges = [[0,1,3]]
k = 2

"""
n = 3
edges = [[0,1,2],[1,2,4]]
k = 3

n = 3
edges = [[0,2,5]]
k = 2
"""

solution = Solution()
print(solution.minTime(n, edges, k))
