class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        from sortedcontainers import SortedList
        self.seats = SortedList()
        self.N = n

    def seat(self):
        """
        :rtype: int
        """
        maxi, maxi_idx = 0, -1
        if len(self.seats) == 0:
            res = 0
        else:
            idx = 0
            maxi = self.seats[idx]
            while idx < len(self.seats) - 1:
                gap = (self.seats[idx + 1] - self.seats[idx]) // 2
                if gap > maxi:
                    maxi, maxi_idx = gap, idx
                idx += 1
            if len(self.seats) > 0:
                gap = (self.N - 1) - self.seats[-1]
                if gap > maxi:
                    maxi, maxi_idx = gap, self.N

            if maxi_idx == -1:
                res = 0
            elif maxi_idx == self.N:
                res = self.N - 1
            else:
                res = self.seats[maxi_idx] + maxi
        self.seats.add(res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

"""
er = ExamRoom(10)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(4)
print(er.seat())
"""

"""
er = ExamRoom(10 ** 9)
print(er.seat())
print(er.seat())
er.leave(0)
print(er.seat())
print(er.seat())
er.leave(499999999)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(874999999)
print(er.seat())
"""

er = ExamRoom(10)
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(0)
er.leave(4)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(0)
er.leave(4)
print(er.seat())
print(er.seat())
er.leave(7)
print(er.seat())
er.leave(3)
print(er.seat())
er.leave(3)
print(er.seat())
er.leave(9)
print(er.seat())
er.leave(0)
er.leave(8)
print(er.seat())
print(er.seat())
er.leave(0)
er.leave(8)
print(er.seat())
print(er.seat())
er.leave(2)
