class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        N = len(quality)

        workers = list()
        for x in range(N):
            workers.append((wage[x] * 1.0 / quality[x], quality[x], wage[x]))
        workers = sorted(workers, key=lambda x: x[0])

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        ans = float("inf")
        for x in range(N):
            ratio = workers[x][0]
            heappush(heap, workers[x][1] * -1)
            while len(heap) > k:
                heappop(heap)
            if len(heap) == k:
                total = sum(heap) * - 1
                ans = min(ans, total * ratio)
        return ans


quality = [10,20,5]
wage = [70,50,30]
k = 2

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3

solution = Solution()
print(solution.mincostToHireWorkers(quality, wage, k))
