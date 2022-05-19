class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        reds = defaultdict(list)
        for edge in redEdges:
            reds[edge[0]].append(edge[1])
        blues = defaultdict(list)
        for edge in blueEdges:
            blues[edge[0]].append(edge[1])

        def doPath(target):
            from collections import deque
            bfs = deque()
            visited = list()
            for vertex in reds[0]:
                bfs.append((vertex, "red", 1))
                visited.append((vertex, "red"))
            for vertex in blues[0]:
                bfs.append((vertex, "blue", 1))
                visited.append((vertex, "blue"))
            while bfs:
                curr, color, length = bfs.popleft()
                if curr == target:
                    return length
                else:
                    if color == "red":
                        for vertex in blues[curr]:
                            if (vertex, "blue") not in visited:
                                bfs.append((vertex, "blue", length + 1))
                                visited.append((vertex, "blue"))
                    elif color == "blue":
                        for vertex in reds[curr]:
                            if (vertex, "red") not in visited:
                                bfs.append((vertex, "red", length + 1))
                                visited.append((vertex, "red"))
            return -1

        anses = [0] * n
        for x in range(n):
            if x != 0:
                ans = doPath(x)
                anses[x] = ans
        return anses


n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []

n = 3
redEdges = [[0,1]]
blueEdges = [[2,1]]

n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]

n = 5
redEdges = [[2,0],[4,3],[4,4],[3,0],[1,4]]
blueEdges = [[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]

solution = Solution()
print(solution.shortestAlternatingPaths(n, redEdges, blueEdges))
