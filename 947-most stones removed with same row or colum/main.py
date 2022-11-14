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

    def get_sets(self):
        return len(set(self.parents))


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        L = len(stones)

        from collections import defaultdict
        rows = defaultdict(list)
        columns = defaultdict(list)
        for idx, stone in enumerate(stones):
            rows[stone[0]].append(idx)
            columns[stone[1]].append(idx)

        ufs = UnionFindSet(L)
        for idx, stone in enumerate(stones):
            if stone[0] in rows:
                ufs.union(idx, rows[stone[0]][0])
            if stone[1] in columns:
                ufs.union(idx, columns[stone[1]][0])

        for idx, _ in enumerate(stones):
            ufs.find(idx)

        ans = L - ufs.get_sets()
        return ans


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
stones = [[0,0]]
stones = [[0,1],[1,0],[1,1]]
stones = [[0,0],[0,1],[1,0]]
stones = [[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]
stones = [[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]
stones = [[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]
stones = [[13,22],[2,29],[19,12],[17,27],[3,0],[3,11],[25,11],[3,21],[27,17],[18,19],[23,12],[5,1],[27,2],[24,0],[8,5],[13,21],[29,27],[16,17],[10,8],[19,18],[20,12],[18,27],[12,24],[2,23],[28,29],[17,24],[24,6],[12,10],[4,0],[6,15],[15,15],[12,3],[14,2],[2,6],[7,12],[26,26],[4,5],[20,26],[11,9],[15,10],[14,15],[18,28],[29,4],[6,12],[3,26],[0,8],[6,5],[15,24],[4,15],[15,21],[5,20],[20,28],[23,0],[5,27],[2,3],[8,27],[2,4]]

solution = Solution()
print(solution.removeStones(stones))
