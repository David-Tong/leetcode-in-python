class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        # helper function
        # get diameter of a tree
        def getDiameter(edges):
            if len(edges) == 0:
                return 0

            # pre-process
            from collections import defaultdict
            dicts = defaultdict(set)
            for edge in edges:
                dicts[edge[0]].add(edge[1])
                dicts[edge[1]].add(edge[0])

            # process
            # step 1 - use bfs to get the farthest node from the start node
            #          which must be one of the node for the tree diameter
            from collections import deque
            bfs = deque()
            bfs.append(edges[0][0])
            visited = set()
            visited.add(edges[0][0])

            while bfs:
                size = len(bfs)
                for _ in range(size):
                    curr = bfs.popleft()
                    for nxt in dicts[curr]:
                        if nxt not in visited:
                            bfs.append(nxt)
                            visited.add(nxt)
                s = curr

            # step 2 - use s node get in the step 1 to get its farthest node
            # step 2 - use s node get in the step 1 to get its farthest node
            #          which must be the another node for the tree diameter
            bfs = deque()
            bfs.append(s)
            visited = set()
            visited.add(s)

            diameter = -1
            while bfs:
                size = len(bfs)
                diameter += 1
                for _ in range(size):
                    curr = bfs.popleft()
                    for nxt in dicts[curr]:
                        if nxt not in visited:
                            bfs.append(nxt)
                            visited.add(nxt)
                t = curr
            return diameter

        diameter1 = getDiameter(edges1)
        diameter2 = getDiameter(edges2)

        ans = max(diameter1, max(diameter2, (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1))
        return ans


edges1 = [[0,1],[0,2],[0,3]]
edges2 = [[0,1]]

edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

solution = Solution()
print(solution.minimumDiameterAfterMerge(edges1, edges2))
