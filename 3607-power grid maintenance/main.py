class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.ranks[px] > self.ranks[py]:
                self.parents[py] = px
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True


class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        # ufs
        ufs = UnionFindSet(c + 1)
        for connection in connections:
            ufs.union(connection[0], connection[1])
        for x in range(c):
            ufs.find(x + 1)

        from collections import defaultdict
        dicts = defaultdict(list)
        for x in range(c):
            dicts[ufs.parents[x + 1]].append(x + 1)
        # print(dicts)

        components = defaultdict(int)
        reports = defaultdict(int)
        for x in dicts:
            reports[x] = 0
            for y in dicts[x]:
                components[y] = x

        # helper function
        def report(component):
            idx = reports[component]
            while idx < len(dicts[component]):
                grid = dicts[component][idx]
                if onlines[grid]:
                    reports[component] = idx
                    return grid
                idx += 1
            return -1

        # process
        ans = list()
        onlines = [True for _ in range(c + 1)]
        for query in queries:
            type, grid = query
            component = components[grid]
            if type == 1:
                if onlines[grid]:
                    ans.append(grid)
                else:
                    ans.append(report(component))
            elif type == 2:
                onlines[grid] = False
        return ans


c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

c = 3
connections = []
queries = [[1,1],[2,1],[1,1]]

solution = Solution()
print(solution.processQueries(c, connections, queries))

