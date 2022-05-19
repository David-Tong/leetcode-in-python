class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        edges = defaultdict(set)

        for connection in connections:
            edges[connection[0]].add(connection[1])
            edges[connection[1]].add(connection[0])

        jumps = [-1] * n
        anses = list()

        def dfs(curr, parent, steps, jumps, anses, edges):
            jumps[curr] = steps + 1
            for child in edges[curr]:
                if child == parent:
                    continue
                elif jumps[child] == -1:
                    jumps[curr] = min(jumps[curr], dfs(child, curr, steps + 1, jumps, anses, edges))
                else:
                    jumps[curr] = min(jumps[curr], jumps[child])

            if jumps[curr] == steps + 1 and curr != 0:
                anses.append([parent, curr])

            return jumps[curr]

        dfs(0, -1, 0, jumps, anses, edges)
        return anses


n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

n = 2
connections = [[0,1]]

solution = Solution()
print(solution.criticalConnections(n, connections))
