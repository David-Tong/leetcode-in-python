class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        M = len(grid)
        N = len(grid[0])
        ans = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N):
                new_x = (x + (y + k) // N) % M
                new_y = (y + k) % N
                ans[new_x][new_y] = grid[x][y]
        return ans


grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 100

solution = Solution()
print(solution.shiftGrid(grid, k))
