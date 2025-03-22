from collections import defaultdict


class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # pre-process
        from collections import defaultdict
        pres = defaultdict(list)
        ingrees = [0] * numCourses
        for prerequisite in prerequisites:
            pres[prerequisite[0]].append(prerequisite[1])
            ingrees[prerequisite[1]] += 1

        # process
        # topological sort
        from collections import deque
        bfs = deque()
        visited = [False] * numCourses
        dependencies = [set() for _ in range(numCourses)]

        for x in range(numCourses):
            if ingrees[x] == 0:
                bfs.append(x)
                visited[x] = True

        while bfs:
            curr = bfs.popleft()
            for x in pres[curr]:
                ingrees[x] -= 1
                dependencies[x].add(curr)
                dependencies[x].update(dependencies[curr])
                if ingrees[x] == 0:
                    bfs.append(x)
                    visited[x] = True

        # print(dependencies)

        # post-process
        ans = list()
        for query in queries:
            if query[0] in dependencies[query[1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]

numCourses = 2
prerequisites = []
queries = [[1,0],[0,1]]

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

numCourses = 4
prerequisites = [[2,3],[2,1],[0,3],[0,1]]
queries = [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]

solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))
