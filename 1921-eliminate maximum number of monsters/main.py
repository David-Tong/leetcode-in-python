class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # pre-process
        L = len(dist)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        for x in range(L):
            heappush(heap, dist[x] * 1.0 / speed[x])

        # run
        ans = 0
        while heap:
            curr = heappop(heap)
            if curr > ans:
                ans += 1
            else:
                return ans
        return ans


dist = [1,3,4]
speed = [1,1,1]

dist = [1,1,2,3]
speed = [1,1,1,1]

dist = [3,2,4]
speed = [5,3,2]

dist = [1,2,3]
speed = [1,2,3]

solution = Solution()
print(solution.eliminateMaximum(dist, speed))
