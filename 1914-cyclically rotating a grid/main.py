class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        S = min(M // 2, N // 2)

        # process
        for s in range(S):
            # collect a layer
            start = (s, s)
            layer = list()
            for y in range(s, N - s):
                layer.append(grid[s][y])
            for x in range(s + 1, M - s - 1):
                layer.append(grid[x][N - s - 1])
            for y in range(N - s - 1, s - 1, -1):
                layer.append(grid[M - s -1][y])
            for x in range(M - s - 2, s, -1):
                layer.append(grid[x][s])

            # rotate a layer
            L = len(layer)
            idx = k % L
            for y in range(s, N - s):
                grid[s][y] = layer[idx]
                idx = (idx + 1) % L
            for x in range(s + 1, M - s - 1):
                grid[x][N - s - 1] = layer[idx]
                idx = (idx + 1) % L
            for y in range(N - s - 1, s - 1, -1):
                grid[M - s -1][y] = layer[idx]
                idx = (idx + 1) % L
            for x in range(M - s - 2, s, -1):
                grid[x][s] = layer[idx]
                idx = (idx + 1) % L

        return grid


grid = [[40,10],[30,20]]
k = 1

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2

grid = [[1,2,3,4],[16,1,2,5],[15,8,3,6],[14,7,4,7],[13,6,5,8],[12,11,10,9]]
k = 1

solution = Solution()
print(solution.rotateGrid(grid, k))
