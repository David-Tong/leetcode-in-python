class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        schedules = list()
        heapify(schedules)

        for interval in intervals:
            start, end = interval
            heappush(schedules, (start, 0))
            heappush(schedules, (end, 1))

        # process
        groups = 0
        ans = 0
        while schedules:
            _, indicator = heappop(schedules)
            if indicator == 0:
                groups += 1
                ans = max(ans, groups)
            else:
                groups -= 1
        return ans


intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
intervals = [[1,3],[5,6],[8,10],[11,13]]
intervals = [[1,1]]


solution = Solution()
print(solution.minGroups(intervals))
