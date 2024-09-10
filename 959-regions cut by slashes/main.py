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
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        # pre-process
        N = len(grid)
        ufs = UnionFindSet(N * N * 4)

        for row in range(N):
            for col in range(N):
                # split a cell into 4 pieces, 0 for top, 1 for right, 2 for down, 3 for left
                idx = row * N * 4 + col * 4

                # process inner connection
                if grid[row][col] == "/":
                    # merge 0, 3
                    ufs.union(idx, idx + 3)
                    # merge 1, 2
                    ufs.union(idx + 1, idx + 2)
                elif grid[row][col] == "\\":
                    # merge 0, 1
                    ufs.union(idx, idx + 1)
                    # merge 2, 3
                    ufs.union(idx + 2, idx + 3)
                else:
                    # merge all 4
                    ufs.union(idx, idx + 1)
                    ufs.union(idx + 1, idx + 2)
                    ufs.union(idx + 2, idx + 3)

                # process inter connection
                # horizontal connection
                # merge 1 on the left and 3 on the right
                if col < N - 1:
                    idx_right = idx + 4
                    ufs.union(idx + 1, idx_right + 3)

                # vertical connection
                # merge 2 on the top and 0 on the down
                if row < N - 1:
                    idx_down = idx + 4 * N
                    ufs.union(idx + 2, idx_down)

        # process
        for x in range(N * N * 4):
            ufs.find(x)

        ans = len(set(ufs.parents))
        return ans


grid = [" /","/ "]
grid = [" /","  "]
grid = ["/\\","\\/"]
grid = ["/\\","\\/"]
grid = ["//","/ "]
grid = ["/\\\\","\\//","\\\\\\"]

solution = Solution()
print(solution.regionsBySlashes(grid))
