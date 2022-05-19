class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        N = numCourses
        courses = [[0, []] for _ in range(N)]

        # process prerequisite
        for prerequisite in prerequisites:
            courses[prerequisite[0]][0] += 1
            courses[prerequisite[1]][1].append(prerequisite)

        # bfs
        from collections import deque
        bfs = deque()
        visited = []
        for idx, course in enumerate(courses):
            if course[0] == 0:
                bfs.append(idx)
                visited.append(idx)

        while bfs:
            idx = bfs.pop()
            for prerequisite in courses[idx][1]:
                courses[prerequisite[0]][0] -= 1
                if courses[prerequisite[0]][0] == 0 and prerequisite[0] not in visited:
                    bfs.append(prerequisite[0])
                    visited.append(prerequisite[0])

        if len(visited) == N:
            return visited
        else:
            return []


numCourses = 2
prerequisites = [[1,0]]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

numCourses = 1
prerequisites = []

numCourses = 2
prerequisites = [[1,0],[0,1]]

solution = Solution()
print(solution.findOrder(numCourses, prerequisites))
