class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        # dp[x][y] - min sum of a falling path to grid[x][y]
        dp = [[float("inf")] * N for _ in range(M)]
        for y in range(N):
            dp[0][y] = grid[0][y]

        # transfer
        for x in range(1, M):
            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)
            for y in range(N):
                heappush(heap, (dp[x - 1][y], y))
            for y in range(N):
                if y == heap[0][1]:
                    top, idx = heappop(heap)
                    dp[x][y] = heap[0][0] + grid[x][y]
                    heappush(heap, (top, idx))
                else:
                    dp[x][y] = heap[0][0] + grid[x][y]
        print(dp)

        ans = min(dp[M - 1])
        return ans


grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[7]]
grid = [[2,3,4,5,6],[11,-5,-7,1,3],[3,4,5,-11,9],[-19,0,11,2,3],[-20,2,3,4,5]]

solution = Solution()
print(solution.minFallingPathSum(grid))
