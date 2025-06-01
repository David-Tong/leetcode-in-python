class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        # bfs
        def getDistances(edges):
            from collections import defaultdict
            paths = defaultdict(set)
            for edge in edges:
                paths[edge[0]].add(edge[1])
                paths[edge[1]].add(edge[0])

            n = len(paths)
            distances = [[0] * n for _ in range(n)]

            for x in range(n):
                from collections import deque
                bfs = deque()
                visited = [False] * n
                bfs.append(x)
                visited[x] = True
                distance = 0
                while bfs:
                    distance += 1
                    for _ in range(len(bfs)):
                        node = bfs.popleft()
                        for nxt in paths[node]:
                            if not visited[nxt]:
                                distances[x][nxt] = distance
                                visited[nxt] = True
                                bfs.append(nxt)
            return distances

        # process
        distances1 = getDistances(edges1)
        distances2 = getDistances(edges2)

        # print(distances1)
        # print(distances2)

        # get the node with max path less than or equal to k length
        def getMaxi(distances, target):
            n = len(distances)
            maxi = 0
            for x in range(n):
                node_maxi = 0
                for y in range(n):
                    if distances[x][y] <= target:
                        node_maxi += 1
                maxi = max(maxi, node_maxi)
            return maxi

        maxi2 = getMaxi(distances2, k - 1)
        ans = list()
        n = len(distances1)
        for x in range(n):
            maxi = 0
            for y in range(n):
                if distances1[x][y] <= k:
                    maxi += 1
            ans.append(maxi + maxi2)
        return ans


edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2

edges1 = [[0,1],[0,2],[0,3],[0,4]]
edges2 = [[0,1],[1,2],[2,3]]
k = 1

solution = Solution()
print(solution.maxTargetNodes(edges1, edges2, k))
