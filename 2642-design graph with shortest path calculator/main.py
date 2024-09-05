class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        from collections import defaultdict
        self.edges = defaultdict(list)
        for edge in edges:
            self.edges[edge[0]].append((edge[2], edge[1]))
        self.nodes = n

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        self.edges[edge[0]].append((edge[2], edge[1]))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        if node1 == node2:
            return 0

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for edge in self.edges[node1]:
            heappush(heap, edge)

        visited = [False] * self.nodes
        visited[node1] = True
        while heap:
            distance, curr = heappop(heap)
            visited[curr] = True
            if curr == node2:
                return distance

            for delta, node in self.edges[curr]:
                if not visited[node]:
                    heappush(heap, (distance + delta, node))

        for distance, node in heap:
            if node == node2:
                return distance
        return -1


"""
n = 4
edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]

g = Graph(n, edges)
print(g.shortestPath(3,2))
print(g.shortestPath(0,3))
g.addEdge([1,3,4])
print(g.shortestPath(0,3))
"""

n = 13
edges = [[7,2,131570],[9,4,622890],[9,1,812365],[1,3,399349],[10,2,407736],[6,7,880509],[1,4,289656],[8,0,802664],[6,4,826732],[10,3,567982],[5,6,434340],[4,7,833968],[12,1,578047],[8,5,739814],[10,9,648073],[1,6,679167],[3,6,933017],[0,10,399226],[1,11,915959],[0,12,393037],[11,5,811057],[6,2,100832],[5,1,731872],[3,8,741455],[2,9,835397],[7,0,516610],[11,8,680504],[3,11,455056],[1,0,252721]]

g = Graph(n, edges)
print(g.shortestPath(9,3))
g.addEdge([11,1,873094])
print(g.shortestPath(3,10))
