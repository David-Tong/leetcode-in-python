class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        M = len(grid)
        N = len(grid[0])

        # calculate stop matrix
        stop = [[False for _ in range(N)] for _ in range(M)]
        for x in range(M):
            for y in range(N):
                # redirect the ball into either wall of the box
                if y == 0 and grid[x][y] == -1:
                    stop[x][y] = True
                    continue
                if y == N - 1 and grid[x][y] == 1:
                    stop[x][y] = True
                    continue

                # get ball stuck in the "V" shape
                if grid[x][y] == 1 and grid[x][y + 1] == -1:
                    stop[x][y] = True
                    continue
                if grid[x][y] == -1 and grid[x][y - 1] == 1:
                    stop[x][y] = True
                    continue

        # bfs
        from collections import deque
        bfs = deque()
        for x in range(N):
            # start col, row, col
            bfs.append((x, 0, x))

        ans = [-1] * N
        while bfs:
            start_col, row, col = bfs.popleft()
            if row == M:
                ans[start_col] = col
                continue

            if not stop[row][col]:
                bfs.append((start_col, row + 1, col + grid[row][col]))
        return ans


grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid = [[-1]]
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

solution = Solution()
print(solution.findBall(grid))
