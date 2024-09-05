class UnionFindSet(object):
    def __init__(self, N):
        self.N = N
        self.parents = [_ for _ in range(N)]
        self.ranks = [0] * N

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        N = len(strs)
        ufs = UnionFindSet(N)

        def diffStr(str, str2):
            difference = 0
            for x in range(len(str)):
                if str[x] != str2[x]:
                    difference += 1
            return difference

        for x in range(N):
            for y in range(x + 1, N):
                if diffStr(strs[x], strs[y]) <= 2:
                    ufs.union(x, y)

        for x in range(N):
            ufs.find(x)

        groups = set()
        for parent in ufs.parents:
            groups.add(parent)

        return len(groups)


strs = ["tars","rats","arts","star"]
strs = ["omv","ovm"]
strs = ["ooo","ooo"]

solution = Solution()
print(solution.numSimilarGroups(strs))