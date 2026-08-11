class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # process
        idx = 0
        grid = [[0]]

        from copy import deepcopy
        while idx < n:
            # calculate grids
            l = len(grid)
            grids = list()

            for _ in range(4):
                grids.append(deepcopy(grid))
                for x in range(l):
                    for y in range(l):
                        grid[x][y] += l * l

            # combine grids together
            grid = [[0] * 2 ** l for _ in range(2 ** l)]
            # top left
            for x in range(l):
                for y in range(l):
                    grid[x][y] = grids[3][x][y]
            # top right
            for x in range(l):
                for y in range(l, 2 * l):
                    grid[x][y] = grids[0][x][y - l]
            # bottom left
            for x in range(l, 2 * l):
                for y in range(l):
                    grid[x][y] = grids[2][x - l][y]
            # bottom right
            for x in range(l, 2 * l):
                for y in range(l, 2 * l):
                    grid[x][y] = grids[1][x - l][y - l]

            idx += 1
            # print(grids)

        ans = grid
        return ans


n = 0
n = 1
n = 2

solution = Solution()
print(solution.specialGrid(n))
