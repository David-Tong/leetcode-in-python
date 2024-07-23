class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # pre-process
        meetings = sorted(meetings)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        rooms = list(range(n))
        heapify(rooms)

        from collections import defaultdict
        usage = defaultdict(int)

        # process
        for meeting in meetings:
            # release root for finished meetings
            while heap and heap[0][0] <= meeting[0]:
                _, room = heappop(heap)
                heappush(rooms, room)

            # make arrangement
            if rooms:
                room = heappop(rooms)
                end = meeting[1]
                heappush(heap, (end, room))
                usage[room] += 1
            else:
                start, room = heappop(heap)
                duration = meeting[1] - meeting[0]
                end = start + duration
                heappush(heap, (end, room))
                usage[room] += 1

        maxi = max(usage.values())
        max_usages = list()
        for key in usage:
            if usage[key] == maxi:
                max_usages.append(key)
        ans = min(max_usages)
        return ans


n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

n = 3
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]

n = 6
meetings = [[0,1],[1,2],[2,3],[3,4],[4,5],[6,7]]

n = 2
meetings = [[0,10],[1,2],[12,14],[13,15]]

n = 4
meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]

n = 3
meetings = [[13,20],[5,17],[17,19]]

solution = Solution()
print(solution.mostBooked(n, meetings))