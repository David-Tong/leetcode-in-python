class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # pre-process
        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
        merges = list()
        start = meetings[0][0]
        limit = meetings[0][1]
        for meeting in meetings[1:]:
            if meeting[0] <= limit:
                limit = max(limit, meeting[1])
            else:
                merges.append((start, limit))
                start = meeting[0]
                limit = meeting[1]
        merges.append((start, limit))

        # process
        ans = merges[0][0] - 1
        for x in range(len(merges) - 1):
            ans += merges[x + 1][0] - merges[x][1] - 1
        ans += days - merges[-1][1]
        return ans


days = 10
meetings = [[5,7],[1,3],[9,10]]

days = 5
meetings = [[2,4],[1,3]]

days = 6
meetings = [[1,6]]

days = 20
meetings = [[5,17],[1,3],[9,14],[15,19]]

solution = Solution()
print(solution.countDays(days, meetings))
