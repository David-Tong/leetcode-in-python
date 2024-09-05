class UnionFindSet(object):
    def __init__(self, N):
        self.N = N
        self.parents = [_ for _ in range(N)]
        self.ranks = [0] * N

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x, y = x - 1, y - 1
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
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def isFullyTraverable(ufs):
            for x in range(len(ufs.parents)):
                ufs.find(x)

            for x in range(1, len(ufs.parents)):
                if ufs.parents[x] != ufs.parents[x - 1]:
                    return False
            return True

        # pre-process
        from collections import defaultdict
        edges_dict = defaultdict(list)
        for edge in edges:
            edges_dict[edge[0]].append((edge[1], edge[2]))

        # ufs
        ufs_alice = UnionFindSet(n)
        ufs_bob = UnionFindSet(n)

        # search type 3
        ans = 0
        for edge in edges_dict[3]:
            if not ufs_alice.union(edge[0], edge[1]):
                ans += 1
            ufs_bob.union(edge[0], edge[1])

        if isFullyTraverable(ufs_alice):
            return ans + len(edges_dict[1]) + len(edges_dict[2])

        # search type 1
        for edge in edges_dict[1]:
            if not ufs_alice.union(edge[0], edge[1]):
                ans += 1

        if not isFullyTraverable(ufs_alice):
            return -1

        # search type 2
        for edge in edges_dict[2]:
            if not ufs_bob.union(edge[0], edge[1]):
                ans += 1

        if not isFullyTraverable(ufs_bob):
            return -1

        return ans


n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]

n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]

n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]

n = 1
edges = [[3,1,1]]

solution = Solution()
print(solution.maxNumEdgesToRemove(n, edges))
