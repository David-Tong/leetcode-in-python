class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # process
        # dijkstra's algorithm
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        visited = [[False] * N for _ in range(M)]
        heappush(heap, (0, 0, 0))

        while heap:
            cost, x, y = heappop(heap)
            # end condition
            if x == M - 1 and y == N - 1:
                return cost
            if not visited[x][y]:
                visited[x][y] = True
                for idx, d in enumerate(DIRECTIONS):
                    dx, dy = d
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if not visited[nx][ny]:
                            addon = 0
                            if idx + 1 != grid[x][y]:
                                addon = 1
                            heappush(heap, (cost + addon, nx, ny))
        return -1


grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
grid = [[1,1,3],[3,2,2],[1,1,4]]
grid = [[1,2],[4,3]]

solution = Solution()
print(solution.minCost(grid))
