class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        M = len(grid)
        N = len(grid[0])

        # dp[x][y][z] - the number of path sum can be divided by z
        dp = [[[0] * k for _ in range(N)] for _ in range(M)]

        # init
        remainders = [[0] * N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                remainder = grid[x][y] % k
                remainders[x][y] = remainder
        dp[0][0][remainders[0][0]] = 1

        # do dp
        for x in range(M):
            for y in range(N):
                for u in range(k):
                    v = remainders[x][y]
                    z = (u + v) % k
                    if x > 0:
                        dp[x][y][z] += dp[x - 1][y][u]
                    if y > 0:
                        dp[x][y][z] += dp[x][y - 1][u]

        return dp[x][y][0] % MODULO


grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3

grid = [[0,0]]
k = 5

grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
k = 1

solution = Solution()
print(solution.numberOfPaths(grid, k))
