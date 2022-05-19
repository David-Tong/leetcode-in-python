class UnionFindSet(object):

    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def coexist(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        else:
            return False

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
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        edges = []
        for x in range(N):
            for y in range(x+1, N):
                distance = abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
                edges.append((distance, (x, y)))
        edges = sorted(edges)

        ufs = UnionFindSet(N)

        ans = 0
        for edge in edges:
            if not ufs.coexist(edge[1][0], edge[1][1]):
                ans += edge[0]
                ufs.union(edge[1][0], edge[1][1])
        return ans


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]

solution = Solution()
print(solution.minCostConnectPoints(points))
