class SummaryRanges(object):

    def __init__(self):
        self.lefts = list()
        self.rights = list()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        # check if need to merge interval
        from bisect import bisect_left
        idx = bisect_left(self.lefts, value)

        if idx > 0:
            if self.lefts[idx - 1] < value <= self.rights[idx - 1]:
                return

        if idx < len(self.lefts):
            if self.lefts[idx] == value:
                return

        # merge interval if need
        left = value
        right = value
        merge_left = False
        merge_right = False

        if idx > 0:
            if self.rights[idx - 1] == value - 1:
                left = min(left, self.lefts[idx - 1])
                merge_left = True

        if idx < len(self.lefts):
            if self.lefts[idx] == value + 1:
                right = max(right, self.rights[idx])
                merge_right = True

        if merge_left:
            if merge_right:
                self.rights[idx - 1] = right
                self.lefts = self.lefts[:idx] + self.lefts[idx + 1:]
                self.rights = self.rights[:idx] + self.rights[idx + 1:]
            else:
                self.rights[idx - 1] = right
        else:
            if merge_right:
                self.lefts[idx] = left
            else:
                self.lefts = self.lefts[:idx] + [left] + self.lefts[idx:]
                self.rights = self.rights[:idx] + [right] + self.rights[idx:]

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        intervals = list()
        for x in range(len(self.lefts)):
            intervals.append([self.lefts[x], self.rights[x]])
        return intervals


"""
sr = SummaryRanges()
sr.addNum(1)
print(sr.getIntervals())
sr.addNum(3)
print(sr.getIntervals())
sr.addNum(7)
print(sr.getIntervals())
sr.addNum(2)
print(sr.getIntervals())
sr.addNum(6)
print(sr.getIntervals())
"""

"""
sr = SummaryRanges()
sr.addNum(1)
print(sr.getIntervals())
sr.addNum(3)
print(sr.getIntervals())
sr.addNum(11)
print(sr.getIntervals())
sr.addNum(2)
print(sr.getIntervals())
sr.addNum(7)
print(sr.getIntervals())
sr.addNum(9)
print(sr.getIntervals())
"""

sr = SummaryRanges()
sr.addNum(1)
print(sr.getIntervals())
sr.addNum(2)
print(sr.getIntervals())
sr.addNum(5)
print(sr.getIntervals())
sr.addNum(6)
print(sr.getIntervals())
sr.addNum(3)
print(sr.getIntervals())
sr.addNum(4)
print(sr.getIntervals())