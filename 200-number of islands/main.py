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

        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        N = len(grid)
        M = len(grid[0])
        ufs = UnionFindSet(N * M)

        for x in range(N):
            for y in range(M):
                if grid[x][y] == "1":
                    if x + 1 < N and grid[x + 1][y] == "1":
                        ufs.union(x * M + y, (x + 1) * M + y)
                    if y + 1 < M and grid[x][y + 1] == "1":
                        ufs.union(x * M + y, x * M + y + 1)

        islands = set()
        for x in range(N):
            for y in range(M):
                if grid[x][y] == "1":
                    islands.add(ufs.find(x * M + y))
        return len(islands)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","1","1","1"],
  ["1","1","0","0","1"],
  ["0","0","1","0","0"],
  ["1","1","1","1","1"]
]

grid = [
  ["1","1","1","1","1"],
  ["1","0","1","0","1"],
  ["0","0","1","0","0"],
  ["1","1","1","1","1"]
]

solution = Solution()
print(solution.numIslands(grid))
