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
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        # build ufs
        ufs = UnionFindSet(n)
        for method, method2 in invocations:
            ufs.union(method, method2)

        # map each method to its group parent
        from collections import defaultdict
        group_map = defaultdict(list)
        for method in range(n):
            parent = ufs.find(method)
            group_map[parent].append(method)

        # process
        # use BFS to find all suspicious methods
        graph = defaultdict(list)
        for method, method2 in invocations:
            graph[method].append(method2)

        from collections import deque
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)

        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    queue.append(nxt)

        # determine suspicious groups
        suspicious_groups = set(ufs.find(x) for x in suspicious)

        # check removal condition
        # no outside method may invoke inside suspicious set
        for method, method2 in invocations:
            if method2 in suspicious and method not in suspicious:
                return list(range(n))

        ans = [_ for _ in range(n) if _ not in suspicious]
        return ans


n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]

n = 5
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4]]

n = 3
k = 2
invocations = [[1,2],[0,1],[2,0]]

n = 6
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4],[5,0]]

solution = Solution()
print(solution.remainingMethods(n, k, invocations))
