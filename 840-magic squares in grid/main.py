class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        rows = [[0] * (N + 1) for _ in range(M)]
        cols = [[0] * (M + 1) for _ in range(N)]

        for x in range(M):
            for y in range(N):
                rows[x][y + 1] = rows[x][y] + grid[x][y]

        for y in range(N):
            for x in range(M):
                cols[y][x + 1] = cols[y][x] + grid[x][y]

        # verify magic square
        def verify_magic_square(sx, sy, ex, ey):
            # check unique number 1 to 9
            from collections import defaultdict
            dicts = defaultdict(bool)
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    dicts[grid[x][y]] = True
            for x in range(9):
                if not dicts[x + 1]:
                    return False

            # check magic value
            MAGIC_VALUE = rows[sx][ey + 1] - rows[sx][sy]
            # check rows
            for x in range(sx, ex + 1):
                if rows[x][ey + 1] - rows[x][sy] != MAGIC_VALUE:
                    return False
            # check columns
            for y in range(sy, ey + 1):
                if cols[y][ex + 1] - cols[y][sx] != MAGIC_VALUE:
                    return False
            # check both diagnoals
            if grid[sx][sy] + grid[sx + 1][sy + 1] + grid[ex][ey] != MAGIC_VALUE:
                return False
            if grid[sx][ey] + grid[sx + 1][ey - 1] + grid[ex][sy] != MAGIC_VALUE:
                return False
            return True

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                if x + 2 < M and y + 2 < N:
                    if verify_magic_square(x, y, x + 2, y + 2):
                        ans += 1
        return ans


grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
grid = [[8]]
grid = [[5,5,5],[5,5,5],[5,5,5]]

solution = Solution()
print(solution.numMagicSquaresInside(grid))
