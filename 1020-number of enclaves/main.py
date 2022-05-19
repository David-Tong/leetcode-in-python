class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def doIsland(x, y):
            enclaves = 0
            from collections import deque
            bfs = deque()
            bfs.append((x, y))
            visited = [(x, y)]
            while bfs:
                x, y = bfs.popleft()
                # fill not closed land to water
                grid[x][y] = 0
                enclaves += 1
                for direction in DIRECTIONS:
                    new_x = x + direction[0]
                    new_y = y + direction[1]
                    if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                        if grid[new_x][new_y] == 1:
                            if (new_x, new_y) not in visited:
                                bfs.append((new_x, new_y))
                                visited.append((new_x, new_y))
            return enclaves

        # fill out all not closed lands
        for x in range(M):
            for y in range(N):
                if x == 0 or x == M - 1:
                    if grid[x][y] == 1:
                        doIsland(x, y)
                elif y == 0 or y == N - 1:
                    if grid[x][y] == 1:
                        doIsland(x, y)

        # count islands
        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    ans += doIsland(x, y)
        return ans


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

solution = Solution()
print(solution.numEnclaves(grid))
