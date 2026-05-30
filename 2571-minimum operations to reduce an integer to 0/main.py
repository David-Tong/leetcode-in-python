class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # process
        from collections import defaultdict
        cache = defaultdict(int)

        def dfs(n):
            if n in cache:
                return cache[n]
            if n == 0:
                res = 0
            elif n == 1:
                res = 1
            else:
                if n % 2 == 0:
                    res = dfs(n // 2)
                else:
                    res = 1 + min(dfs(n // 2), dfs((n + 1)// 2))
            cache[n] = res
            return cache[n]

        return dfs(n)


n = 39
n = 54

solution = Solution()
print(solution.minOperations(n))
