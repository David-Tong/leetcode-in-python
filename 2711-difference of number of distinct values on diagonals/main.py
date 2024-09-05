class Solution(object):
    def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(grid)
        N = len(grid[0])

        ans = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                # search top-left diagonal
                nx, ny = x - 1, y - 1
                top_lefts = set()
                while nx >= 0 and ny >= 0:
                    top_lefts.add(grid[nx][ny])
                    nx, ny = nx - 1, ny - 1

                # search bottom-right diagonal
                nx, ny = x + 1, y + 1
                bottom_rights = set()
                while nx < M and ny < N:
                    bottom_rights.add(grid[nx][ny])
                    nx, ny = nx + 1, ny + 1

                ans[x][y] = abs(len(top_lefts) - len(bottom_rights))
        return ans


grid = [[1,2,3],[3,1,5],[3,2,1]]
grid = [[1]]
grid = [[1,2,3,5,5],[5,5,1,1,5],[5,5,5,1,1]]


solution = Solution()
print(solution.differenceOfDistinctValues(grid))