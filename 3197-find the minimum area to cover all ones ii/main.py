class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # helper functions
        # find the minimum area to cover all ones in a rectangle
        # the rectangle is from row t to row b - 1, from col l to col r - 1
        def cover(target, t, b, l, r):
            top, bottom = float("inf"), float("-inf")
            left, right = float("inf"), float("-inf")
            for x in range(t, b):
                for y in range(l, r):
                    if target[x][y] == 1:
                        top = min(top, x)
                        bottom = max(bottom, x)
                        left = min(left, y)
                        right = max(right, y)
            res = (bottom - top + 1) * (right - left + 1)
            return res

        # rotate the grid to anti-clock direction by 90 degree
        def rotate():
            rotated = [[0] * M for _ in range(N)]
            for x in range(M):
                for y in range(N):
                    rotated[y][x] = grid[x][y]
            return rotated
        # print(rotate())

        # process
        # there are 6 ways to split a grid
        """
        case 1
            X      
          Y   Z   
        
        case 2
          X   Y
            Z
            
        case 3
            X
            Y
            Z
        """
        # case 1
        ans = float("inf")
        for x in range(1, M):
            for y in range(1, N):
                ans = min(ans, cover(grid, 0, x, 0, N)
                          + cover(grid, x, M, 0, y)
                          + cover(grid, x, M, y, N))

        # case 2
        for x in range(1, M):
            for y in range(1, N):
                ans = min(ans, cover(grid, 0, x, 0, y)
                          + cover(grid, 0, x, y, N)
                          + cover(grid, x, M, 0, N))

        # case 3
        for x in range(1, M):
            for y in range(x + 1, M):
                ans = min(ans, cover(grid, 0, x, 0, N)
                          + cover(grid, x, y, 0, N)
                          + cover(grid, y, M, 0, N))

        # rotate and handle the other 3 cases
        """
        case 4
             Y
          X      
             Z   

        case 5
          X   
             Z
          Y
        
        case 6
          XYZ
        """
        rotated = rotate()
        # case 4
        for x in range(1, N):
            for y in range(1, M):
                ans = min(ans, cover(rotated, 0, x, 0, M)
                          + cover(rotated, x, N, 0, y)
                          + cover(rotated, x, N, y, M))

        # case 5
        for x in range(1, N):
            for y in range(1, M):
                ans = min(ans, cover(rotated, 0, x, 0, y)
                          + cover(rotated, 0, x, y, M)
                          + cover(rotated, x, N, 0, M))

        # case 6
        for x in range(1, N):
            for y in range(x + 1, N):
                ans = min(ans, cover(rotated, 0, x, 0, M)
                          + cover(rotated, x, y, 0, M)
                          + cover(rotated, y, N, 0, M))

        return ans


grid = [[1,0,1],[1,1,1]]
grid = [[1,0,1,0],[0,1,0,1]]
grid = [[0,1,0,1],[0,1,0,0],[0,1,0,1]]

from random import randint
grid = [[randint(0, 1) for _ in range(30)] for _ in range(30)]
print(grid)


solution = Solution()
print(solution.minimumSum(grid))
