class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses

        from collections import defaultdict
        in_degrees = defaultdict(list)
        out_degrees = defaultdict(list)

        for prerequisite in prerequisites:
            if not prerequisite[0] in in_degrees:
                in_degrees[prerequisite[0]] = list()
            in_degrees[prerequisite[0]].append(prerequisite[1])
            if not prerequisite[1] in out_degrees:
                out_degrees[prerequisite[1]] = list()
            out_degrees[prerequisite[1]].append(prerequisite[0])

        from collections import deque
        queue = deque()
        for in_degree in in_degrees:
            degrees[in_degree] = len(in_degrees[in_degree])

        for idx, vertex in enumerate(degrees):
            if vertex == 0:
                queue.append(idx)

        while queue:
            node = queue.popleft()
            for vertex in out_degrees[node]:
                degrees[vertex] -= 1
                if degrees[vertex] == 0:
                    queue.append(vertex)

        for vertex in degrees:
            if vertex != 0:
                return False
        return True


numCourses = 2
prerequisites = [[1,0]]

#numCourses = 2
prerequisites = [[1,0],[0,1]]

numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]

solution = Solution()
print(solution.canFinish(numCourses, prerequisites))
