class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        # scan rows
        from collections import defaultdict
        rows = defaultdict(int)
        for x in range(M):
            key = ""
            for y in range(N):
                if y != N - 1:
                    key += str(grid[x][y]) + "-"
                else:
                    key += str(grid[x][y])
            rows[key] += 1

        # scan columns
        columns = defaultdict(int)
        for y in range(N):
            key = ""
            for x in range(M):
                if x != M - 1:
                    key += str(grid[x][y]) + "-"
                else:
                    key += str(grid[x][y])
            columns[key] += 1

        ans = 0
        for key in rows:
            if key in columns:
                ans += rows[key] * columns[key]
        return ans


grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid = [[1]]

solution = Solution()
print(solution.equalPairs(grid))
