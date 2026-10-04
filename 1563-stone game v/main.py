class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        # pre-process
        L = len(stoneValue)
        presums = list()
        presums.append(0)
        for value in stoneValue:
            presums.append(presums[-1] + value)

        # dfs
        from collections import defaultdict
        self.cache = defaultdict(int)

        def dfs(start, end):
            key = "{}-{}".format(start, end)
            if key in self.cache:
                return self.cache[key]

            if start == end:
                return 0
            res = 0
            for x in range(start + 1, end):
                left_total = presums[x] - presums[start]
                right_total = presums[end] - presums[x]
                if left_total <= right_total:
                    res = max(res, left_total + dfs(start, x))
                if left_total >= right_total:
                    res = max(res, right_total + dfs(x, end))
            self.cache[key] = res
            return res

        # process
        ans = dfs(0, L)
        return ans


stoneValue = [6,2,3,4,5,5]
stoneValue = [7,7,7,7,7,7,7]
stoneValue = [4]

"""
from random import randint
stoneValue = [randint(1, 10 ** 6) for _ in range(500)]
print(stoneValue)
"""

stoneValue = [39994,3,4,10000,10000,10000,10000,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000000]

solution = Solution()
print(solution.stoneGameV(stoneValue))
