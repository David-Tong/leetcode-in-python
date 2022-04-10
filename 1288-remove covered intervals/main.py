class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x : (x[0], -x[1]))
        upper = 0
        count = 0
        for interval in intervals:
            if interval[1] > upper:
                count += 1
                upper = interval[1]
        return count


intervals = [[1, 4], [3, 6], [2, 8], [2, 4]]
intervals = [[1, 4], [3, 6], [2, 8]]
intervals = [[1, 4], [2, 3]]
intervals = [[1, 4]]
intervals = [[1, 4], [2, 5]]
intervals = [[2, 4], [1, 3]]

solution = Solution()
print(solution.removeCoveredIntervals(intervals))
