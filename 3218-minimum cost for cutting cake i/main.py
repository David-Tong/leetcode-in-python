class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        # memorized dfs
        from collections import defaultdict
        self.cache = defaultdict(int)

        def dfs(r1, c1, r2, c2):
            key = "{}-{}-{}-{}".format(r1, c1, r2, c2)
            if key in self.cache:
                return self.cache[key]

            if r1 + 1 == r2 and c1 + 1 == c2:
                return 0

            res = float("inf")
            for h in range(r1 + 1, r2):
                res = min(res, dfs(r1, c1, h, c2) + dfs(h, c1, r2, c2) + horizontalCut[h - 1])
            for c in range(c1 + 1, c2):
                res = min(res, dfs(r1, c1, r2, c) + dfs(r1, c, r2, c2) + verticalCut[c - 1])

            self.cache[key] = res
            return res

        return dfs(0, 0, m, n)


m = 3
n = 2
horizontalCut = [1,3]
verticalCut = [5]

m = 2
n = 2
horizontalCut = [7]
verticalCut = [4]

"""
m = 3
n = 3
horizontalCut = [564,472]
verticalCut = [581,319]

m = 5
n = 5
horizontalCut = [100, 29, 52, 97]
verticalCut = [52, 64, 20, 20]

m = 4
n = 4
horizontalCut = [2,4,4]
verticalCut = [7,8,4]

m = 4
n = 4
from random import randint
horizontalCut = [randint(1, 10) for _ in range(m - 1)]
verticalCut = [randint(1, 10) for _ in range(n -1)]
print(horizontalCut)
print(verticalCut)
"""

solution = Solution()
print(solution.minimumCost(m, n, horizontalCut, verticalCut))
