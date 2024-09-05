class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        N = len(colors)
        C = 26
        from collections import defaultdict
        out_edges = defaultdict(list)
        in_degress = [0] * N

        for edge in edges:
            out_edges[edge[0]].append(edge[1])
            in_degress[edge[1]] += 1

        # dynamic programming
        # dp[x][y] - the max number of node of color y for the path ended with node x
        dp = [[0] * C for _ in range(N)]

        # topology sort
        from collections import deque
        queue = deque()
        for vertex in range(N):
            if in_degress[vertex] == 0:
                queue.append(vertex)
                color_idx = ord(colors[vertex]) - ord('a')
                dp[vertex][color_idx] = 1

        ans = 0
        while queue:
            curr = queue.popleft()
            ans = max(ans, max(dp[curr]))
            for node in out_edges[curr]:
                in_degress[node] -= 1
                if in_degress[node] == 0:
                    queue.append(node)
                for color_idx in range(C):
                    if color_idx == ord(colors[node]) - ord('a'):
                        dp[node][color_idx] = max(dp[node][color_idx], dp[curr][color_idx] + 1)
                    else:
                        dp[node][color_idx] = max(dp[node][color_idx], dp[curr][color_idx])

        if sum(in_degress) == 0:
            return ans
        else:
            return -1


colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

colors = "a"
edges = [[0,0]]

colors = "a"
edges = []

colors = 'bacabacaa'
edges = [[0,2],[1,3],[1,4],[2,3],[2,4],[3,7],[4,5],[4,6],[6,8]]

colors = 'bacaaaaaa'
edges = [[0,2],[1,3],[1,4],[2,3],[2,4],[3,7],[4,5],[4,6],[6,8]]

solution = Solution()
print(solution.largestPathValue(colors, edges))
