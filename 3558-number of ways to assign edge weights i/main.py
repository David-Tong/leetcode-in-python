class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        from collections import defaultdict
        dicts = defaultdict(list)
        for edge in edges:
            mini = min(edge[0], edge[1])
            maxi = max(edge[0], edge[1])
            dicts[mini].append(maxi)

        # bfs
        from collections import deque
        bfs = deque()
        bfs.append(1)

        depth = -1
        while bfs:
            for _ in range(len(bfs)):
                vertex = bfs.popleft()
                for nxt in dicts[vertex]:
                    bfs.append(nxt)
            depth += 1
        # print(depth)

        # process
        ans = 1
        for _ in range(depth - 1):
            ans = ans * 2 % MODULO
        return ans


edges = [[1,2]]
edges = [[1,2],[1,3],[3,4],[3,5]]

solution = Solution()
print(solution.assignEdgeWeights(edges))
