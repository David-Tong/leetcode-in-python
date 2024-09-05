class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        edges = defaultdict(list)
        for road in roads:
            edges[road[0]].append((road[1], road[2]))
            edges[road[1]].append((road[0], road[2]))

        # bfs
        from collections import deque
        bfs = deque()
        visited = [False] * (n + 1)
        bfs.append(1)
        visited[1] = True

        while bfs:
            node = bfs.popleft()
            for edge in edges[node]:
                if not visited[edge[0]]:
                    visited[edge[0]] = True
                    bfs.append(edge[0])

        ans = float("inf")
        for idx, vst in enumerate(visited):
            if vst:
                for edge in edges[idx]:
                    ans = min(ans, edge[1])
        return ans


n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]

n = 5
roads = [[1,2,10],[2,4,12],[3,5,1]]

n = 2
roads = [[1,2,10]]

solution = Solution()
print(solution.minScore(n, roads))
