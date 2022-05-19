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
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        N = len(s)
        ufs = UnionFindSet(N)
        for pair in pairs:
            ufs.union(pair[0], pair[1])

        from collections import defaultdict
        components = defaultdict(list)

        # components[][0] - idx list, components[][1] - english letter list, for the component
        for node in range(N):
            parent = ufs.find(node)
            if not parent in components:
                components[parent].append(list())
                components[parent].append(list())
            components[parent][0].append(node)
            components[parent][1].append(s[node])

        ans = [""] * N
        for component in components:
            idx2 = 0
            letters = sorted(components[component][1])
            for idx in components[component][0]:
                ans[idx] = letters[idx2]
                idx2 += 1
        return "".join(ans)


s = "dcab"
pairs = [[0,3],[1,2]]

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]

s = "cba"
pairs = [[0,1],[1,2]]

s = "a"
pairs = []

solution = Solution()
print(solution.smallestStringWithSwaps(s, pairs))
