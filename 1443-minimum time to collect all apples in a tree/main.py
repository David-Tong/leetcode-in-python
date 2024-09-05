class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        from collections import defaultdict
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        visited = [False] * n

        def doMinTime(vertex):
            time = 0
            visited[vertex] = True
            for node in tree[vertex]:
                if not visited[node]:
                    time += doMinTime(node)
            if vertex != 0:
                if time > 0 or hasApple[vertex]:
                    time += 2
            return time

        return doMinTime(0)


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,False,False,False,False,False]

n = 1
edges = []
hasApple = [True]

n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False,True,False,False]

solution = Solution()
print(solution.minTime(n, edges, hasApple))
