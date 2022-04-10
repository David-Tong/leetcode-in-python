class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x : (x[0], -x[1]))
        right = intervals[0][1]
        ans = 0
        for interval in intervals[1:]:
            if interval[0] < right:
                right = min(right, interval[1])
                ans += 1
            else:
                right = interval[1]
        return ans


intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
#intervals = [[1,2],[2,3]]
#intervals = [[1,100],[11,22],[1,11],[2,12]]
#intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]

solution = Solution()
print(solution.eraseOverlapIntervals(intervals))
