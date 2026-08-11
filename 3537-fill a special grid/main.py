class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # process
        grid = [[0]]

        idx = 0
        while idx < n:
            k = 4 ** idx
            l = 2 ** idx
            nl = l * 2
            ngrid = [[0] * nl for _ in range(nl)]
            for x in range(nl):
                for y in range(nl):
                    # top left
                    if 0 <= x < l:
                        if 0 <= y < l:
                            ngrid[x][y] = grid[x][y] + 3 * k
                    # top right
                    if 0 <= x < l:
                        if l <= y < 2 * l:
                            ngrid[x][y] = grid[x][y - l]
                    # bottom left
                    if l <= x < 2 * l:
                        if 0 <= y < l:
                            ngrid[x][y] = grid[x - l][y] + 2 * k
                    # bottom right
                    if l <= x < 2 * l:
                        if l <= y < 2 * l:
                            ngrid[x][y] = grid[x - l][y - l] + k
            grid = ngrid
            # print(grid)
            idx += 1

        ans = grid
        return ans


n = 0
n = 1
n = 2

solution = Solution()
print(solution.specialGrid(n))
