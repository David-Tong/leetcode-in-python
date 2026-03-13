class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        graph = defaultdict(defaultdict)
        for u, v, cost in edges:
            if u in graph and v in graph[u]:
                graph[u][v] = min(graph[u][v], cost)
            else:
                graph[u][v] = cost
            if v in graph and u in graph[v]:
                graph[v][u] = min(graph[v][u], cost * 2)
            else:
                graph[v][u] = cost * 2
        # print(graph)

        # process
        distances = [-1] * n
        from heapq import heapify, heappop, heappush
        heap = list()
        heapify(heap)
        heappush(heap, (0, 0))

        while heap:
            distance, vertex = heappop(heap)
            if vertex == n - 1:
                return distance
            if distances[vertex] == -1:
                distances[vertex] = distance
                for nxt in graph[vertex]:
                    if distances[nxt] == -1:
                        heappush(heap, (distance + graph[vertex][nxt], nxt))
        return -1

n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

n = 4
edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

n = 2
edges = [[0,1,17],[1,0,12]]

solution = Solution()
print(solution.minCost(n, edges))
