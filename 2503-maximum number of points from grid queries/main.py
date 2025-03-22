class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        from collections import defaultdict
        dicts = defaultdict(int)

        # process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        visited = [[False] * N for _ in range(M)]
        heappush(heap, (grid[0][0], 0, 0))

        current = grid[0][0]
        count = 0
        while heap:
            value, x, y = heappop(heap)
            if not visited[x][y]:
                if value > current:
                    dicts[current] = count
                    current = value
                count += 1

                visited[x][y] = True
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N:
                        if not visited[nx][ny]:
                            heappush(heap, (grid[nx][ny], nx, ny))
        dicts[current] = count

        # post-process
        keys = sorted(dicts.keys())
        values = list()
        for key in keys:
            values.append(dicts[key])
        # print(keys)
        # print(values)

        from bisect import bisect_left
        ans = list()
        for query in queries:
            idx = bisect_left(keys, query)
            if idx > 0:
                ans.append(values[idx - 1])
            else:
                ans.append(0)
        return ans


grid = [[1,2,3],[2,5,7],[3,5,1]]
queries = [5,6,2]

grid = [[5,2,1],[1,1,2]]
queries = [3]

grid = [[420766,806051,922751],[181527,815280,904568],[952102,4037,140319],[324081,17907,799523],[176688,90257,83661],[932477,621193,623068],[135839,554701,511427],[227575,450848,178065],[785644,204668,835141],[313774,167359,501496],[641317,620688,74989],[324499,122376,270369],[2121,887154,848859],[456704,7763,662087],[286827,145349,468865],[277137,858176,725551],[106131,93684,576512],[372563,944355,497187],[884187,600892,268120],[576578,515031,807686]]
queries = [352655,586228,169685,541073,584647,413832,576537,616413]

solution = Solution()
print(solution.maxPoints(grid, queries))
