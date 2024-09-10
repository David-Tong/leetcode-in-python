class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # short cut
        if source == destination:
            return True

        # process edges
        from collections import defaultdict
        vertices = defaultdict(list)
        for edge in edges:
            vertices[edge[0]].append(edge[1])
            vertices[edge[1]].append(edge[0])

        # bfs
        from collections import deque
        bfs = deque()
        visited = list()
        bfs.append(source)
        visited.append(source)

        while bfs:
            vertex = bfs.popleft()
            for node in vertices[vertex]:
                if node == destination:
                    return True

                if node not in visited:
                    bfs.append(node)
                    visited.append(node)
        return False


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5

n = 1
edges = []
source = 0
destination = 0

solution = Solution()
print(solution.validPath(n, edges, source, destination))
