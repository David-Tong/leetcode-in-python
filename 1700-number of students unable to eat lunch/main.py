class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter = 0
        while counter < len(students):
            if students[0] == sandwiches[0]:
                counter = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                counter += 1
        return len(students)


students = [1,1,0,0]
sandwiches = [0,1,0,1]

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

solution = Solution()
print(solution.countStudents(students, sandwiches))
