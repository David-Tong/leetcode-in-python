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
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        S = UnionFindSet(N)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] == 1:
                    S.union(i, j)

        circles = set()
        for i in range(N):
            circles.add(S.find(i))
        return len(circles)


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

solution = Solution()
print(solution.findCircleNum(isConnected))
