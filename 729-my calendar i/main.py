class MyCalendar(object):

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
            if count > 1:
                return False

        self.books = tmp
        return True


mc = MyCalendar()
print(mc.book(10, 20))
print(mc.book(15, 25))
print(mc.book(20, 30))




