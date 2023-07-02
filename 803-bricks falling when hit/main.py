class UnionFindSet(object):

    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.children = [1] * size

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if px > py:
            self.parents[py] = px
            self.children[px] += self.children[py]
        else:
            self.parents[px] = py
            self.children[py] += self.children[px]
        return True

    def capacity(self, x):
        return self.children[x]


class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        M = len(grid)
        N = len(grid[0])
        ROOF = M * N
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def getIndex(x, y):
            return x * N + y

        # pre-process
        from copy import deepcopy
        updated_grid = deepcopy(grid)

        for hit in hits:
            x, y = hit
            updated_grid[x][y] = 0

        # index M * N is the pseudo node for roof
        ufs = UnionFindSet(M * N + 1)
        for x in range(M):
            for y in range(N):
                if updated_grid[x][y] == 1:
                    if x == 0:
                        ufs.union(getIndex(x, y), ROOF)
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if updated_grid[nx][ny] == 1:
                                ufs.union(getIndex(x, y), getIndex(nx, ny))

        # back in time
        ans = list()
        for hit in hits[::-1]:
            x, y = hit
            if grid[x][y] == 1:
                # before reunion
                prev_children = ufs.capacity(ROOF)

                # reunion
                if x == 0:
                    ufs.union(getIndex(x, y), ROOF)
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if updated_grid[nx][ny] == 1:
                            ufs.union(getIndex(x, y), getIndex(nx, ny))

                # after reunion
                after_children = ufs.capacity(ROOF)

                updated_grid[x][y] = 1

                # update answer
                ans.append(max(0, after_children - prev_children - 1))
            else:
                ans.append(0)

        return ans[::-1]


grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]

grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]

grid = [[1,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0]]
hits = [[2,4],[1,1],[1,3],[0,0]]

grid = [[1,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0]]
hits = [[2,4],[1,1],[1,3],[2,2],[0,0]]

grid = [[1,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0]]
hits = [[2,4],[2,2],[1,1],[1,3],[0,0]]

grid = [[1],[1],[1],[1],[1]]
hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]

grid = [[1,0,1],[1,1,1]]
hits = [[0,0],[0,2],[1,1]]

grid = [[0,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[0,0,0,1,0,0,1,1,1],[0,0,1,1,0,1,1,1,0],[0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,0]]
hits = [[1,8],[2,1],[1,4],[3,0],[3,4],[0,7],[1,6],[0,8],[2,5],[3,2],[2,0],[0,2],[0,5],[0,1],[4,8],[3,7],[0,6],[5,7],[5,3],[2,6],[2,2],[5,8],[2,8],[4,0],[3,3],[1,1],[0,0],[4,7],[0,3],[2,4],[3,1],[1,0],[5,2],[3,8],[4,2],[5,0],[1,2],[1,7],[3,6],[4,1],[5,6],[0,4],[5,5],[5,4],[1,5],[4,4],[3,5],[4,6],[2,3],[2,7]]

grid = [[1,1,1],[0,1,0],[0,0,0]]
hits = [[0,2],[2,0],[0,1],[1,2]]

solution = Solution()
print(solution.hitBricks(grid, hits))
