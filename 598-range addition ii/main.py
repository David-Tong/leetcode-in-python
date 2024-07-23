class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_row = m
        min_col = n

        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])

        return min_row * min_col


m = 3
n = 3
ops = [[2,2],[3,3]]

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]

m = 3
n = 3
ops = []

solution = Solution()
print(solution.maxCount(m, n, ops))
