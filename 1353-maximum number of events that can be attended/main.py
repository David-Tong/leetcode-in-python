class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        L = len(events)

        # get range of days
        start = float("inf")
        end = float("-inf")
        for event in events:
            start = min(start, event[0])
            end = max(end, event[1])

        # sort
        events = sorted(events, key=lambda x: (x[0], -x[1]))

        # heap
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        # search
        idx = 0
        ans = 0
        for x in range(start, end + 1):
            while idx < L and events[idx][0] <= x:
                heappush(heap, events[idx][1])
                idx += 1
            if heap and heap[0] >= x:
                heappop(heap)
                ans += 1
            while heap and heap[0] <= x:
                heappop(heap)
        return ans


events = [[1,2],[2,3],[3,4]]
events = [[1,2],[2,3],[3,4],[1,2]]
events = [[1,2],[2,3],[2,3],[1,2]]
events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
events = [[1,2],[1,2],[1,6],[1,2],[1,2]]

solution = Solution()
print(solution.maxEvents(events))
