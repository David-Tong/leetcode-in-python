class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 1

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return 0


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        # Refer to https://www.youtube.com/watch?v=n3s9Q7GtfB4

        # Euler's formula
        # V - E + F = C + 1 => Ans = F - 1 = E - V + C
        # V - Vertex number, E - Edge number, C - Component number, F - Face number

        def getIndex(row, col):
            return row * (N + 1) + col

        # pre-process
        N = len(grid)
        ufs = UnionFindSet((N + 1) * (N + 1))

        # merge all vertex on the boundary
        for row in range(N + 1):
            for col in range(N + 1):
                idx = getIndex(row, col)
                if row == 0 or row == N or col == 0 or col == N:
                    ufs.union(0, idx)

        # process
        ans = 1
        for row in range(N):
            for col in range(N):
                if grid[row][col] == " ":
                    pass
                elif grid[row][col] == "/":
                    # create a new face only when two vertexes are in the same component already
                    ans += ufs.union(getIndex(row, col + 1), getIndex(row + 1, col))
                else:
                    ans += ufs.union(getIndex(row, col), getIndex(row + 1, col + 1))
        return ans


grid = [" /","/ "]
grid = [" /","  "]
"""
grid = ["/\\","\\/"]
grid = ["/\\","\\/"]
grid = ["//","/ "]
grid = ["/\\\\","\\//","\\\\\\"]
"""

solution = Solution()
print(solution.regionsBySlashes(grid))


