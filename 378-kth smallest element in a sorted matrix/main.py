class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix)

        from heapq import heapify, heappush, heappop
        heap = []
        heapify(heap)
        for x in range(N):
            heappush(heap, (matrix[x][0], (x, 0)))

        while k > 0:
            ans, (row, col) = heappop(heap)
            k -= 1
            if k == 0:
                return ans
            else:
                if col + 1 < N:
                    heappush(heap, (matrix[row][col + 1], (row, col + 1)))

        return ans


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

matrix = [[-5]]
k = 1

solution = Solution()
print(solution.kthSmallest(matrix, k))
