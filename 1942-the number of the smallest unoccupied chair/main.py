from symbol import pass_stmt


class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        # pre-process
        L = len(times)
        from heapq import heapify, heappush, heappop
        schedule = list()
        heapify(schedule)
        seats = [_ for _ in range(L)]
        heapify(seats)

        # process
        # decouple time to in and out
        for idx, t in enumerate(times):
            # in record : start time, indicator, end time, idx
            heappush(schedule, (t[0], 1, t[1], idx))

        while schedule:
            t0, indicator, t2, idx = heappop(schedule)
            # in record
            if indicator == 1:
                end = t2
                seat = heappop(seats)
                if idx == targetFriend:
                    return seat
                # out record : end time, indicator, seat, idx
                heappush(schedule, (end, -1, seat, idx))
            # out record
            elif indicator == -1:
                seat = t2
                heappush(seats, seat)


times = [[1,4],[2,3],[4,6]]
targetFriend = 1

times = [[3,10],[1,5],[2,6]]
targetFriend = 0

times = [[2,5],[7,8],[5,8],[3,4],[1,7]]
targetFriend = 4

solution = Solution()
print(solution.smallestChair(times, targetFriend))
