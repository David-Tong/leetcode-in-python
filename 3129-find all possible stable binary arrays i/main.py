class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        # pre-process
        import sys
        sys.setrecursionlimit(5000)

        MODULO = 10 ** 9 + 7

        # process
        # dfs
        # dfs(i, j, k) - the number of valid arrays with
        #              - i zeros, j ones, and ended with k equals to 0 or 1
        def dfs(i, j, k):
            key = "{}-{}-{}".format(i, j, k)
            if key in self.cache:
                return self.cache[key]

            # end condition
            if i == 0:
                return 1 if j <= limit and k == 1 else 0
            if j == 0:
                return 1 if i <= limit and k == 0 else 0
            if k == 0:
                res = dfs(i - 1, j, 0) + dfs(i - 1, j, 1)
                if i > limit:
                     res -= dfs(i - limit - 1, j, 1)
            else:
                res = dfs(i, j - 1, 0) + dfs(i, j - 1, 1)
                if j > limit:
                    res -= dfs (i, j - limit - 1, 0)

            res = res % MODULO
            self.cache[key] = res
            return res

        # cache
        from collections import defaultdict
        self.cache = defaultdict(int)

        # dfs
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MODULO
        self.cache = None
        return ans


zero = 1
one = 1
limit = 2

zero = 1
one = 2
limit = 1

zero = 3
one = 3
limit = 2

zero = 1000
one = 1000
limit = 50


solution = Solution()
print(solution.numberOfStableArrays(zero, one, limit))
