class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        presums = [[0] for _ in range(M)]
        for x in range(M):
            for y in range(N):
                presums[x].append(presums[x][-1] + grid[x][y])
        # print(presums)

        # process
        ans = float("inf")
        for x in range(N):
            maxi = max(presums[1][x], presums[0][-1] - presums[0][x + 1])
            ans = min(ans, maxi)
        return ans

grid = [[2,5,4],[1,5,1]]
grid = [[3,3,1],[8,5,2]]
grid = [[1,3,1,15],[1,3,3,1]]

solution = Solution()
print(solution.gridGame(grid))
