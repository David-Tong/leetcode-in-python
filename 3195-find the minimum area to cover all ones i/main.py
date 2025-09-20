class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        top, bottom = M, -1
        left, right = N, -1
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    top = min(top, x)
                    bottom = max(bottom, x)
                    left = min(left, y)
                    right = max(right, y)

        # print(top, bottom, left, right)

        # process
        ans = (bottom - top + 1) * (right - left + 1)
        return ans


grid = [[0,1,0],[1,0,1]]
grid = [[1,0],[0,0]]

solution = Solution()
print(solution.minimumArea(grid))

