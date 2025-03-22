from compiler.pyassem import findDepth


class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        for edge in edges:
            dicts[edge[0]].append(edge[1])
            dicts[edge[1]].append(edge[0])

        # process
        graphs = defaultdict(int)

        # search all nodes, find the one as root node can construct the maximum number of groups
        for x in range(n):
            start = x + 1
            max_depth = 0
            smallest_id = float("inf")
            levels = [0] * (n + 1)

            # bfs
            from collections import deque
            # idx, depth
            bfs = deque()
            bfs.append((start, 1))
            levels[start] = 1

            while bfs:
                curr, depth = bfs.popleft()
                max_depth = max(max_depth, depth)
                smallest_id = min(smallest_id, curr)

                for nxt in dicts[curr]:
                    if levels[nxt] == 0:
                        levels[nxt] = depth + 1
                        bfs.append((nxt, depth + 1))
                    # when a cycle exists, you can't divide nodes as required
                    elif levels[nxt] == depth:
                        return -1
            graphs[smallest_id] = max(graphs[smallest_id], max_depth)

        # post-process
        ans = 0
        for id in graphs:
            ans += graphs[id]
        return ans


n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]

n = 3
edges = [[1,2],[2,3],[3,1]]

n = 2
edges = [[1,2]]

solution = Solution()
print(solution.magnificentSets(n, edges))
