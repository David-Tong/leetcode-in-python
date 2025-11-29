class Solution(object):
    def maxSum(self, grid, limits, k):
        """
        :type grid: List[List[int]]
        :type limits: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for x in range(M):
            for y in range(N):
                heappush(heap, (-1 * grid[x][y], x))

        # process
        ans = 0
        while k > 0:
            if heap:
                num, row = heappop(heap)
                if limits[row] > 0:
                    ans -= num
                    limits[row] -= 1
                    k -= 1
        return ans


grid = [[1,2],[3,4]]
limits = [1,2]
k = 2

grid = [[5,3,7],[8,2,6]]
limits = [2,2]
k = 3

solution = Solution()
print(solution.maxSum(grid, limits, k))
