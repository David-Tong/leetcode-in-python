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
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(properties)
        graph = [[False] * L for _ in range(L)]
        from collections import defaultdict
        dicts = defaultdict(set)
        for x in range(L):
            dicts[x] = set(properties[x])

        # process
        ufs = UnionFindSet(L)
        for x in range(L):
            for y in range(x + 1, L):
                if len(dicts[x] & dicts[y]) >= k:
                    ufs.union(x, y)

        for x in range(L):
            ufs.find(x)

        ans = len(set(ufs.parents))
        return ans


properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]]
k = 1

properties = [[1,2,3],[2,3,4],[4,3,5]]
k = 2

properties = [[1,1],[1,1]]
k = 2

solution = Solution()
print(solution.numberOfComponents(properties, k))

