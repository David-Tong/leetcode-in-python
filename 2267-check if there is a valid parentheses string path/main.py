class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # dp[x][y] = the number of valid "(" exists in the path
        dp = [[set()] * N for _ in range(M)]
        if grid[0][0] == ")" or grid[M - 1][N - 1] == "(":
            return False
        else:
            dp[0][0].add(1)

        # transfer
        for x in range(M):
            for y in range(N):
                paths = set()
                if x > 0:
                    if grid[x][y] == "(":
                        for path in dp[x - 1][y]:
                            paths.add(path + 1)
                    else:
                        for path in dp[x - 1][y]:
                            if path > 0:
                                paths.add(path - 1)
                    dp[x][y] = paths

                if y > 0:
                    if grid[x][y] == "(":
                        for path in dp[x][y - 1]:
                            paths.add(path + 1)
                    else:
                        for path in dp[x][y - 1]:
                            if path > 0:
                                paths.add(path - 1)
                    dp[x][y] = paths

        if 0 in dp[M - 1][N - 1]:
            return True
        else:
            return False


grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
grid = [[")",")"],["(","("]]
grid = [["(",")","(","("],["(",")",")","("],[")","(",")",")"],[")","(","(","("],["(",")","(","("],["(",")","(","("],[")",")","(",")"]]

solution = Solution()
print(solution.hasValidPath(grid))
