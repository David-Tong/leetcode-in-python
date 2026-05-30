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
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        # pre-process
        L = len(source)
        ufs = UnionFindSet(L)
        for vertex, vertex2 in allowedSwaps:
            ufs.union(vertex, vertex2)

        for vertex in range(L):
            ufs.find(vertex)

        # print(ufs.parents)
        from collections import defaultdict
        dicts = defaultdict(list)
        for vertex, parent in enumerate(ufs.parents):
            dicts[parent].append(vertex)

        # process
        ans = 0
        for parent in dicts:
            dicts2 = defaultdict(int)
            for vertex in dicts[parent]:
                dicts2[source[vertex]] += 1
            for vertex in dicts[parent]:
                if target[vertex] in dicts2:
                    if dicts2[target[vertex]] > 0:
                        dicts2[target[vertex]] -= 1
            for key in dicts2:
                ans += dicts2[key]
        return ans


source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]

source = [1,2,3,4]
target = [1,3,2,4]
allowedSwaps = []

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]

source = [2,3,1]
target = [1,2,2]
allowedSwaps = [[0,2],[1,2]]

source = [2,2,1]
target = [1,2,3]
allowedSwaps = [[0,2],[1,2]]

solution = Solution()
print(solution.minimumHammingDistance(source, target, allowedSwaps))
