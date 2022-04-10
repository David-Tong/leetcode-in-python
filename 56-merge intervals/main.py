class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)

        mergeds = []
        previous = intervals[0]
        limit = previous[1]
        for interval in intervals[1:]:
            if interval[0] <= limit:
                limit = max(limit, interval[1])
            else:
                mergeds.append([previous[0], limit])
                previous = interval
                limit = previous[1]
        mergeds.append([previous[0], limit])

        return mergeds


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
intervals = [[1, 3], [1, 2], [1, 10]]
intervals = [[1, 3], [4, 6], [7, 10]]
intervals = [[1, 3]]
intervals = [[1, 3], [1, 2], [1, 10], [2, 9]]

solution = Solution()
print(solution.merge(intervals))
