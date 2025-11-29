class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(intervals)
        # sort by ending point
        intervals = sorted(intervals, key=lambda x:(x[1], -x[0]))
        # print(intervals)

        # process
        points = list()
        points.append(intervals[0][1] - 1)
        points.append(intervals[0][1])
        for x in range(1, L):
            start, end = intervals[x]
            if start <= points[-2]:
                # there are two points overlapped
                pass
            elif start <= points[-1]:
                # there are only one point overlapped
                points.append(end)
            else:
                # there are no overlapped points
                points.append(end - 1)
                points.append(end)
        ans = len(points)
        return ans


intervals = [[1,3],[3,7],[8,9]]
intervals = [[1,3],[1,4],[2,5],[3,5]]
intervals = [[1,2],[2,3],[2,4],[4,5]]
intervals = [[1,3],[3,7],[5,7],[7,8]]

solution = Solution()
print(solution.intersectionSizeTwo(intervals))
