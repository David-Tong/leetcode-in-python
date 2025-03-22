class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(events)
        events = sorted(events, key=lambda x: (x[0], x[1], x[2]))
        events2 = sorted(events, key=lambda x: (x[1], x[0], x[2]))

        # process
        from heapq import heapify, heappush
        heap = list()
        heapify(heap)

        idx2 = 0
        ans = 0
        for event in events:
            while events2[idx2][1] < event[0]:
                heappush(heap, -1 * events2[idx2][2])
                idx2 += 1
            if heap:
                ans = max(ans, -1 * heap[0] + event[2])
            else:
                ans = max(ans, event[2])
        return ans


events = [[1,3,2],[4,5,2],[2,4,3]]
events = [[1,3,2],[4,5,2],[1,5,5]]
events = [[1,5,3],[1,5,1],[6,6,5]]
events = [[1,10,10],[2,4,6],[5,7,6]]

solution = Solution()
print(solution.maxTwoEvents(events))
