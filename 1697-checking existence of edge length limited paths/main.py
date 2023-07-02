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

    def connect(self, x, y):
        if self.parents[x] == self.parents[y]:
            return True
        else:
            if self.find(self.parents[x]) == self.find(self.parents[y]):
                return True
        return False


class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        M = len(edgeList)
        N = len(queries)

        # ufs
        ufs = UnionFindSet(n)

        # pre-process
        for idx, query in enumerate(queries):
            query.append(idx)
        edgeList = sorted(edgeList, key=lambda x: (x[2], x[0], x[1]))
        queries = sorted(queries, key=lambda x:(x[2], x[0], x[1]))

        index = 0
        ans = [False] * N
        for query in queries:
            distance = query[2]
            addeds = set()
            while index < M and edgeList[index][2] < distance:
                addeds.add(edgeList[index][0])
                addeds.add(edgeList[index][1])
                ufs.union(edgeList[index][0], edgeList[index][1])
                index += 1

            for added in addeds:
                ufs.find(added)

            ans[query[3]] = ufs.connect(query[0], query[1])
        return ans


n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]

n = 2
edgeList = [[0,1,100]]
queries = [[0,1,100]]

n = 5
edgeList = [[0,1,2],[1,4,14],[2,0,18],[1,0,16]]
queries = [[0,1,15],[0,3,1]]

n = 13
edgeList = [[9,1,53],[3,2,66],[12,5,99],[9,7,26],[1,4,78],[11,1,62],[3,10,50],[12,1,71],[12,6,63],[1,10,63],[9,10,88],[9,11,59],[1,4,37],[4,2,63],[0,2,26],[6,12,98],[9,11,99],[4,5,40],[2,8,25],[4,2,35],[8,10,9],[11,9,25],[10,11,11],[7,6,89],[2,4,99],[10,4,63]]
queries = [[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76],[4,2,15],[7,6,52],[2,0,50],[7,6,62],[1,0,81],[4,5,35],[0,11,86],[12,5,50],[11,2,2],[9,5,6],[12,0,95],[10,6,9],[9,4,73],[6,10,48],[12,0,91],[9,10,58],[9,8,73],[2,3,44],[7,11,83],[5,3,14],[6,2,33]]
#queries = [[3,7,76]]
#queries = [[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76]]

solution = Solution()
print(solution.distanceLimitedPathsExist(n, edgeList, queries))
