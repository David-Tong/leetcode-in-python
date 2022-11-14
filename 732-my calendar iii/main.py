class MyCalendarThree(object):

    def __init__(self):
        self.pivots = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        # update pivots
        from bisect import bisect_left, bisect_right
        idx_right = bisect_right(self.pivots, (start, 1))
        self.pivots = self.pivots[:idx_right] + [(start, 1)] + self.pivots[idx_right:]
        idx_left = bisect_left(self.pivots, (end, -1))
        self.pivots = self.pivots[:idx_left] + [(end, -1)] + self.pivots[idx_left:]

        # get max k-book
        ans = 0
        kbook = 0
        for timestamp, direction in self.pivots:
            kbook += direction
            if direction == 1:
                ans = max(ans, kbook)
        return ans


"""
calendar = MyCalendarThree()
print(calendar.book(10, 20))
print(calendar.book(50, 60))
print(calendar.book(10, 40))
print(calendar.book(5, 15))
print(calendar.book(5, 10))
print(calendar.book(25, 55))
"""

calendar = MyCalendarThree()
print(calendar.book(5, 12))
print(calendar.book(42, 50))
print(calendar.book(4, 9))
print(calendar.book(33, 41))
print(calendar.book(2, 7))
print(calendar.book(16, 25))
print(calendar.book(7, 16))
print(calendar.book(6, 11))
print(calendar.book(13, 18))
print(calendar.book(38, 43))
print(calendar.book(49, 50))
print(calendar.book(6, 15))
print(calendar.book(5, 13))
print(calendar.book(35, 42))
print(calendar.book(19, 24))
print(calendar.book(46, 50))
print(calendar.book(39, 44))
print(calendar.book(28, 36))
print(calendar.book(28, 37))
print(calendar.book(20, 29))
print(calendar.book(41, 49))
print(calendar.book(11, 19))
print(calendar.book(41, 46))
print(calendar.book(28, 37))
print(calendar.book(17, 23))
print(calendar.book(22, 31))
print(calendar.book(4, 10))
print(calendar.book(31, 40))
print(calendar.book(4, 12))
print(calendar.book(19, 26))
