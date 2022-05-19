class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals)

        stack = []
        stack.append(intervals[0])
        limit = intervals[0][1]
        for interval in intervals[1:]:
            if stack and interval[0] <= limit:
                prev = stack.pop()
                limit = max(limit, interval[1])
                stack.append([prev[0], limit])
            else:
                limit = max(limit, interval[1])
                stack.append(interval)

        return stack


intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = []
newInterval = [1,2]

solution = Solution()
print(solution.insert(intervals, newInterval))
