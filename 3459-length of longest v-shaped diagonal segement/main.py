class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        DIRECTIONS = ((-1, 1), (1, 1), (1, -1), (-1, -1))
        M = len(grid)
        N = len(grid[0])

        # process
        from collections import defaultdict
        self.cache = defaultdict(int)
        def dfs(x, y, d, turned):
            key = "{}-{}-{}-{}".format(x, y, d, turned)
            if key in self.cache:
                return self.cache[key]

            maxi = 1
            curr = grid[x][y]

            # keep the direction
            dx, dy = DIRECTIONS[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] == 2 - curr:
                    maxi = max(maxi, dfs(nx, ny, d, turned) + 1)

            # make clockwise 90-degree turn
            if not turned:
                d = (d + 1) % 4
                dx, dy = DIRECTIONS[d]
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if grid[nx][ny] == 2 - curr:
                        maxi = max(maxi, dfs(nx, ny, d, True) + 1)

            self.cache[key] = maxi
            return maxi

        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    ans = max(ans, 1)
                    for d in range(4):
                        dx, dy = DIRECTIONS[d]
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < M and 0 <= ny < N:
                            if grid[nx][ny] == 2:
                                ans = max(ans, dfs(nx, ny, d, False) + 1)
        return ans


grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
grid = [[1]]

from random import randint
grid = [[randint(0, 2) for _ in range(500)] for _ in range(500)]
print(grid)

solution = Solution()
print(solution.lenOfVDiagonal(grid))
