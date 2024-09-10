class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        """
        # pre-process
        from collections import defaultdict
        paths = defaultdict(dict)
        editable = defaultdict(dict)

        for edge in edges:
            if edge[2] == -1:
                paths[edge[0]][edge[1]] = 1
                paths[edge[1]][edge[0]] = 1
                editable[edge[0]][edge[1]] = True
                editable[edge[1]][edge[0]] = True
            else:
                paths[edge[0]][edge[1]] = edge[2]
                paths[edge[1]][edge[0]] = edge[2]
                editable[edge[0]][edge[1]] = False
                editable[edge[1]][edge[0]] = False

        # process
        # dijkstra algorithm
        from heapq import heapify, heappush, heappop

        # calculate the shortest distance to the destination
        heap = list()
        heapify(heap)
        heappush(heap, (0, destination))
        distance_to_destination = [float("inf")] * n

        while heap:
            distance, vertex = heappop(heap)
            if distance_to_destination[vertex] == float("inf"):
                distance_to_destination[vertex] = distance
                for next_vertex in paths[vertex]:
                    if distance_to_destination[next_vertex] == float("inf"):
                        new_distance = distance + paths[vertex][next_vertex]
                        heappush(heap, (new_distance, next_vertex))

        # print(distance_to_destination)

        # calculate the shortest distance from source
        # heap should be empty after the previous run
        heappush(heap, (0, source))
        distance_from_source = [float("inf")] * n
        while heap:
            distance, vertex = heappop(heap)
            if distance_from_source[vertex] == float("inf"):
                distance_from_source[vertex] = distance
                # stop condition, not exist the shortest path equal to target
                if vertex == destination and distance != target:
                    return list()
                for next_vertex in paths[vertex]:
                    if distance_from_source[next_vertex] == float("inf"):
                        # make sure we only create valid shortest paths
                        if editable[vertex][next_vertex] and distance_from_source[vertex] + paths[vertex][next_vertex] + distance_to_destination[next_vertex] < target:
                            new_weight = target - distance_from_source[vertex] - distance_to_destination[next_vertex]
                            paths[vertex][next_vertex] = new_weight
                            paths[next_vertex][vertex] = new_weight
                            new_distance = distance + new_weight
                        else:
                            new_distance = distance + paths[vertex][next_vertex]
                        heappush(heap, (new_distance, next_vertex))

        # post-process
        for edge in edges:
            edge[2] = paths[edge[0]][edge[1]]
        return edges


n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 5

n = 3
edges = [[0,1,-1],[0,2,5]]
source = 0
destination = 2
target = 6

n = 4
edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
source = 0
destination = 2
target = 6

solution = Solution()
print(solution.modifiedGraphEdges(n, edges, source, destination, target))
