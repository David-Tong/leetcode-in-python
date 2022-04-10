class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        M = len(dungeon)
        N = len(dungeon[0])

        dp = [[float("inf")] * (N + 1) for _ in range(M + 1)]
        dp[M][N - 1] = 1
        dp[M - 1][N] = 1

        for x in range(M-1, -1, -1):
            for y in range(N-1, -1, -1):
                dp[x][y] = max(min(dp[x+1][y], dp[x][y+1]) - dungeon[x][y], 1)
        return dp[0][0]


dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[0]]
dungeon = [[100]]
dungeon = [[-3,5]]
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]

solution = Solution()
print(solution.calculateMinimumHP(dungeon))
