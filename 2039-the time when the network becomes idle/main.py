from collections import deque


class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        # pre-process
        N = len(patience)
        from collections import defaultdict
        paths = defaultdict(list)
        for edge in edges:
            paths[edge[0]].append(edge[1])
            paths[edge[1]].append(edge[0])

        # process
        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(0)
        visited = [False] * N
        visited[0] = True

        ans = 0
        steps = 0
        while bfs:
            steps += 2
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                for nxt in paths[curr]:
                    if not visited[nxt]:
                        if patience[nxt] < steps:
                            latency = ((steps - 1)// patience[nxt]) * patience[nxt]
                        else:
                            latency = 0
                        ans = max(ans, steps + latency)
                        visited[nxt] = True
                        bfs.append(nxt)
        ans += 1
        return ans


edges = [[0,1],[1,2]]
patience = [0,2,1]

edges = [[0,1],[0,2],[1,2]]
patience = [0,10,10]

edges = [[0,1],[1,2]]
patience = [0,3,1]

solution = Solution()
print(solution.networkBecomesIdle(edges, patience))
