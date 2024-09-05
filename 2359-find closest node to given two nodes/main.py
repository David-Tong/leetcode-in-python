class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        L = len(edges)
        distances1 = [-1] * L
        distances2 = [-1] * L

        def doDistance(edges, node, distances):
            from collections import deque
            bfs = deque()
            visited = [False] * L

            bfs.append(node)
            visited[node] = True

            distance = 0
            while bfs:
                N = len(bfs)
                for x in range(N):
                    curr = bfs.popleft()
                    distances[curr] = distance
                    if edges[curr] != -1 and not visited[edges[curr]]:
                        bfs.append(edges[curr])
                        visited[edges[curr]] = True
                distance += 1

        doDistance(edges, node1, distances1)
        doDistance(edges, node2, distances2)

        ans = -1
        mini = float("inf")
        for x in range(L):
            if distances1[x] != -1 and distances2[x] != -1:
                if mini > max(distances1[x], distances2[x]):
                    ans = x
                    mini = max(distances1[x], distances2[x])
        return ans


edges = [2,2,3,-1]
node1 = 0
node2 = 1

edges = [1,2,-1]
node1 = 0
node2 = 2

edges = [1,0]
node1 = 0
node2 = 1

edges = [9,8,7,0,5,6,1,3,2,2]
node1 = 1
node2 = 6

solution = Solution()
print(solution.closestMeetingNode(edges, node1, node2))
