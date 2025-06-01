class Solution(object):
    def maxTargetNodes(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        # coloring algorithm
        def coloringNodes(edges):
            # pre-process
            from collections import defaultdict
            paths = defaultdict(set)
            nodes = defaultdict(int)
            for edge in edges:
                paths[edge[0]].add(edge[1])
                paths[edge[1]].add(edge[0])
            N = len(paths)

            # bfs
            from collections import deque
            bfs = deque()
            visited = [False] * N
            bfs.append(0)
            visited[0] = True
            color = 0
            nodes[0] = color

            while bfs:
                color = 1 - color
                for _ in range(len(bfs)):
                    curr = bfs.popleft()
                    for nxt in paths[curr]:
                        if not visited[nxt]:
                            bfs.append(nxt)
                            nodes[nxt] = color
                            visited[nxt] = True
            return nodes

        # counts
        def countNodes(nodes):
            from collections import defaultdict
            counts = defaultdict(int)
            for node in nodes:
                counts[nodes[node]] += 1
            return counts

        # process
        nodes1, nodes2 = coloringNodes(edges1), coloringNodes(edges2)
        counts1, counts2 = countNodes(nodes1), countNodes(nodes2)

        ans = list()
        maxi = max(counts2.values())
        for node in nodes1:
            color = nodes1[node]
            ans.append(counts1[color] + maxi)
        return ans


edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

edges1 = [[0,1],[0,2],[0,3],[0,4]]
edges2 = [[0,1],[1,2],[2,3]]

solution = Solution()
print(solution.maxTargetNodes(edges1, edges2))
