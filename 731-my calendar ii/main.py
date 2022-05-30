class MyCalendarTwo(object):

    def __init__(self):
        self.books = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        tmp = list()
        tmp.extend(self.books)
        tmp.append((start, 1))
        tmp.append((end, -1))
        tmp = sorted(tmp, key=lambda x: (x[0], x[1]))

        count = 0
        for time, oper in tmp:
            count += oper
            if count > 2:
                return False

        self.books = tmp
        return True


mct = MyCalendarTwo()
print(mct.book(10, 20))
print(mct.book(50, 60))
print(mct.book(10, 40))
print(mct.book(5, 15))
print(mct.book(5, 10))
print(mct.book(25, 55))
