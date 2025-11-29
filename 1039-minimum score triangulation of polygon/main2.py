class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        # process
        L = len(values)

        # dfs with cache
        from collections import defaultdict
        self.cache = defaultdict(int)

        # the minimal score for triangulation for point x to point y
        def dfs(x, y):
            if y - x < 2:
                return 0

            key = "{}-{}".format(x, y)
            if key in self.cache:
                return self.cache[key]

            res = float("inf")
            for k in range(x + 1, y):
                res = min(res, dfs(x, k) + values[x] * values[y] * values[k] + dfs(k, y))

            self.cache[key] = res
            return res

        return dfs(0, L - 1)


values = [1,2,3]
values = [3,7,4,5]
values = [1, 3, 1, 4, 1, 5]

solution = Solution()
print(solution.minScoreTriangulation(values))
