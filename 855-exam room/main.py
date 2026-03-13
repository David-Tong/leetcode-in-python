class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.N = n
        self.students = list()

    def seat(self):
        """
        :rtype: int
        """
        if not self.students:
            allocated_student = 0
        else:
            maxi_distance, allocated_student = self.students[0], 0
            for idx, student in enumerate(self.students):
                if idx > 0:
                    prev_student = self.students[idx-1]
                    distance = (student - prev_student) // 2
                    if distance > maxi_distance:
                        maxi_distance, allocated_student = distance, prev_student + distance
            distance = self.N - 1 - self.students[-1]
            if distance > maxi_distance:
                allocated_student = self.N - 1

        from bisect import insort
        insort(self.students, allocated_student)
        return allocated_student

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

er = ExamRoom(10)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
er.leave(4)
print(er.seat())