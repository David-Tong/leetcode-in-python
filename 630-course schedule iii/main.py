class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key=lambda x: x[1])
        days = 0

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for course in courses:
            heappush(heap, course[0] * -1)
            days += course[0]
            if days > course[1]:
                to_remove = heappop(heap)
                days += to_remove

        return len(heap)


courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
courses = [[3,2],[4,3]]

solution = Solution()
print(solution.scheduleCourse(courses))
