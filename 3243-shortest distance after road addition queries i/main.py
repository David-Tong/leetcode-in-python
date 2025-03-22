class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        START, END = 0, n - 1
        from collections import defaultdict
        adjacencies = defaultdict(dict)
        for x in range(n):
            for y in range(x + 1, n):
                if x + 1 == y:
                    adjacencies[x][y] = True

        # process
        def shortestDistsnce():
            from collections import deque
            bfs = deque()
            bfs.append(START)
            from collections import defaultdict
            visited = defaultdict(bool)
            visited[START] = True

            steps = 0
            while bfs:
                steps += 1
                size = len(bfs)
                for _ in range(size):
                    curr = bfs.popleft()
                    for nxt in adjacencies[curr]:
                        if nxt == END:
                            return steps
                        if not visited[nxt]:
                            bfs.append(nxt)
                            visited[nxt] = True

        ans = list()
        for query in queries:
            adjacencies[query[0]][query[1]] = True
            ans.append(shortestDistsnce())
        return ans


n = 5
queries = [[2,4],[0,2],[0,4]]

n = 4
queries = [[0,3],[0,2]]

solution = Solution()
print(solution.shortestDistanceAfterQueries(n, queries))
