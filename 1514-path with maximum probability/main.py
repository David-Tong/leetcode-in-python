class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)

        for idx, edge in enumerate(edges):
            dicts[edge[0]].append((edge[1], succProb[idx]))
            dicts[edge[1]].append((edge[0], succProb[idx]))

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append((start, 1))
        visited = [0] * n
        visited[start] = 1

        ans = 0
        while bfs:
            curr, prob = bfs.popleft()
            for idx in range(len(dicts[curr])):
                n_vertex = dicts[curr][idx][0]
                n_prob = prob * dicts[curr][idx][1]
                # update answer
                if n_vertex == end:
                    ans = max(ans, n_prob)
                else:
                    if n_prob > visited[n_vertex]:
                        bfs.append((n_vertex, n_prob))
                        visited[n_vertex] = n_prob
        return ans


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

solution = Solution()
print(solution.maxProbability(n, edges, succProb, start, end))
