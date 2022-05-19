class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        colors = [0] * N

        def doColor(graph, colors, idx):
            from collections import deque
            bfs = deque()
            bfs.append((idx, 1))
            colors[idx] = 1
            while bfs:
                vertex, color = bfs.popleft()
                for next_vertex in graph[vertex]:
                    if colors[next_vertex] == 0:
                        colors[next_vertex] = -1 * color
                        bfs.append((next_vertex, -1 * color))
                    else:
                        if color * colors[next_vertex] == 1:
                            return False
            return True

        # color vertexs
        for idx, edges in enumerate(graph):
            if colors[idx] == 0:
                if not doColor(graph, colors, idx):
                    return False

        return True


graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
graph = [[],[2],[1,3],[2]]

solution = Solution()
print(solution.isBipartite(graph))
