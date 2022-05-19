class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)

        from collections import defaultdict
        in_edges = defaultdict(list)
        out_degrees = [0] * N
        for idx, vertices in enumerate(graph):
            out_degrees[idx] = len(vertices)
            for vertex in vertices:
                in_edges[vertex].append(idx)

        with_terminal_node = True
        anses = list()
        while with_terminal_node:
            with_terminal_node = False
            for idx, out_degree in enumerate(out_degrees):
                if out_degree == 0:
                    with_terminal_node = True
                    for vertex in in_edges[idx]:
                        out_degrees[vertex] -= 1
                    out_degrees[idx] = -1
                    anses.append(idx)
        return sorted(anses)


graph = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

solution = Solution()
print(solution.eventualSafeNodes(graph))
