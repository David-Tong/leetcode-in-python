class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # get the last number less than it
        N = len(arr)
        intervals = list()
        for x in range(N):
            has_less = False
            for y in range(N - 1, x, -1):
                if arr[y] < arr[x]:
                    intervals.append((x, y))
                    has_less = True
                    break
            if not has_less:
                intervals.append((x, x))

        # merge intervals
        limit = intervals[0][1]
        ans = 1
        for interval in intervals:
            if interval[0] <= limit:
                limit = max(limit, interval[1])
            else:
                ans += 1
                limit = interval[1]
        return ans