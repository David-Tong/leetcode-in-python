class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        diffs = [[0] * n for _ in range(n)]

        for query in queries:
            r1, c1, r2, c2 = query
            for row in range(r1, r2 + 1):
                diffs[row][c1] += 1
                if c2 < n - 1:
                    diffs[row][c2 + 1] -= 1

        # process
        ans = [[0] * n for _ in range(n)]
        for row in range(n):
            item = 0
            for col in range(n):
                item += diffs[row][col]
                ans[row][col] = item
        return ans


n = 3
queries = [[1,1,2,2],[0,0,1,1]]

n = 2
queries = [[0,0,1,1]]

solution = Solution()
print(solution.rangeAddQueries(n, queries))
