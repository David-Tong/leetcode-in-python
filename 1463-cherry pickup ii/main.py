class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        # dp[x][y][z] - maximum number of cherries collected when robot #1 and # 2
        #             - at row x, #1 at column y, #2 at column z
        dp = [[[float("-inf")] * N for _ in range(N)] for _ in range(M)]
        dp[0][0][N - 1] = grid[0][0] + grid[0][N - 1]

        for x in range(1, M):
            for y in range(N):
                for z in range(N):
                    for i in range(-1, 2, 1):
                        for j in range(-1, 2, 1):
                            if 0 <= y + i < N and 0 <= z + j < N:
                                if y != z:
                                    dp[x][y][z] = max(dp[x][y][z], dp[x - 1][y + i][z + j] + grid[x][y] + grid[x][z])
                                else:
                                    dp[x][y][z] = max(dp[x][y][z], dp[x - 1][y + i][z + j] + grid[x][y])

        print(dp)
        # ans
        ans = 0
        for y in range(N):
            for z in range(N):
                ans = max(ans, dp[-1][y][z])
        return ans


grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
grid = [[4,7,5,0,10,8,6],[7,8,1,4,3,8,8],[3,2,9,3,4,8,10],[5,4,1,9,9,8,8],[3,6,8,0,10,4,5],[1,9,1,9,5,7,5],[1,4,9,2,5,4,3],[8,9,6,9,10,2,7],[3,2,1,0,3,1,6],[4,2,2,3,8,0,1]]
grid = [[0,8,7,10,9,10,0,9,6],[8,7,10,8,7,4,9,6,10],[8,1,1,5,1,5,5,1,2],[9,4,10,8,8,1,9,5,0],[4,3,6,10,9,2,4,8,10],[7,3,2,8,3,3,5,9,8],[1,2,6,5,6,2,0,10,0]]
grid = [[0,8,7,10,9,10,0,9,6],[8,7,10,8,7,4,9,6,10],[8,1,1,5,1,5,5,1,2],[9,4,10,8,8,1,9,5,0],[4,3,6,10,9,2,4,8,10]]

solution = Solution()
print(solution.cherryPickup(grid))
