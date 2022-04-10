class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        ALL_VISITED = (1 << len(graph)) - 1

        from collections import deque
        bfs = deque()

        visited = set()
        for x in range(len(graph)):
            bfs.append((x, 1 << x))

        steps = 0
        while bfs:
            length = len(bfs)
            for x in range(length):
                curr = bfs.popleft()
                if curr[1] == ALL_VISITED:
                    return steps
                if curr not in visited:
                    visited.add(curr)
                    for next in graph[curr[0]]:
                        bfs.append((next, 1 << next | curr[1]))
            steps += 1
        return steps


graph = [[1, 2, 3], [0], [0], [0]]
graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
graph = [[2, 3, 7], [3, 6], [0, 4], [0, 1, 4, 5], [3, 7, 2, 6], [3], [4, 1], [4, 0]]
graph = [[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]]

solution = Solution()
print(solution.shortestPathLength(graph))
