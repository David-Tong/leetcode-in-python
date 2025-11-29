class CountIntervals(object):

    def __init__(self):
        from sortedcontainers import SortedDict
        self.intervals = SortedDict()
        self.cnt = 0

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        idx = self.intervals.bisect_left(left)
        while idx < len(self.intervals) and self.intervals.values()[idx] <= right:
            r, l = self.intervals.keys()[idx], self.intervals.values()[idx]
            left = min(left, l)
            right = max(right, r)
            self.cnt -= r - l + 1
            self.intervals.popitem(idx)
        self.cnt += right - left + 1
        self.intervals[right] = left

    def count(self):
        """
        :rtype: int
        """
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

ci = CountIntervals()
ci.add(2, 3)
#ci.add(7, 10)
ci.add(6, 7)
print(ci.count())
ci.add(5, 8)
print(ci.count())
