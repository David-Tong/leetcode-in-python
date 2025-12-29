class UnionFindSet(object):
    def __init__(self, size):
        self.size = size
        self.parents = [_ for _ in range(size)]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if px > py:
                self.parents[py] = px
            else:
                self.parents[px] = py
            return True

    def connected(self, x, y):
        return self.parents[x] == self.parents[y]


class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # pre-process
        L = len(nums)
        ufs = UnionFindSet(n)
        from bisect import bisect_right
        for x in range(L):
            target = nums[x] + maxDiff
            idx = bisect_right(nums, target)
            if nums[idx - 1] - nums[x] <= maxDiff:
                if idx - 1 != x:
                    ufs.union(x, idx - 1)

        # process
        for x in range(L):
            ufs.find(x)

        ans = list()
        for query in queries:
            x, y = query[0], query[1]
            ans.append(ufs.connected(x, y))
        return ans


n = 2
nums = [1,3]
maxDiff = 1
queries = [[0,0],[0,1]]

n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]

from random import randint
n = 10 ** 4
nums = [randint(0, n) for _ in range(n)]
nums = sorted(nums)
queries = [(randint(0, n - 1), randint(0, n - 1)) for _ in range(n)]
maxDiff = 5000

print(nums)
print(queries)

solution = Solution()
print(solution.pathExistenceQueries(n, nums, maxDiff, queries))
