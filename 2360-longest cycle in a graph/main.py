class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        N = len(edges)
        degrees = [0] * N

        for edge in edges:
            if edge >= 0:
                degrees[edge] += 1

        # topological sort
        from collections import deque
        queue = deque()
        for vertex, degree in enumerate(degrees):
            if degree == 0:
                queue.append(vertex)

        while queue:
            vertex = queue.popleft()
            if edges[vertex] >= 0:
                degrees[edges[vertex]] -= 1
                if degrees[edges[vertex]] == 0:
                    queue.append(edges[vertex])

        # bfs
        from collections import deque
        bfs = deque()
        visited = [False] * N
        for vertex, degree in enumerate(degrees):
            if degree == 0:
                visited[vertex] = True

        ans = -1
        for idx in range(N):
            if not visited[idx]:
                cycle = 0
                bfs.append(idx)
                visited[idx] = True

                while bfs:
                    vertex = bfs.popleft()
                    cycle += 1
                    if not visited[edges[vertex]]:
                        bfs.append(edges[vertex])
                        visited[edges[vertex]] = True
                    else:
                        if cycle > 1:
                            ans = max(ans, cycle)
        return ans


edges = [3,3,4,2,3]
edges = [2,-1,3,1]
edges = [1,2,3,4,5,6,7,8,9,10,0]
edges = [1,2,3,4,5,0,7,8,9,10,0]


solution = Solution()
print(solution.longestCycle(edges))