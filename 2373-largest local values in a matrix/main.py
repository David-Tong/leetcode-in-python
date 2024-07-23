class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        def getLargestLocal(x, y):
            maxi = 0
            for dx in range(3):
                for dy in range(3):
                    maxi = max(maxi, grid[x + dx][y + dy])
            return maxi

        # process
        ans = [[0] * (N - 2) for _ in range(M - 2)]
        for x in range(M - 2):
            for y in range(N - 2):
                ans[x][y] = getLargestLocal(x, y)
        return ans


grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

solution = Solution()
print(solution.largestLocal(grid))
