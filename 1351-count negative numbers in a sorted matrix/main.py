class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])

        first_columns = list()
        for x in range(M):
            first_columns.append(grid[x][0])

        from bisect import bisect_left
        idx_columns = bisect_left(first_columns[::-1], 0)

        ans = idx_columns * N
        for x in range(M - idx_columns):
            idx_rows = bisect_left(grid[x][::-1], 0)
            ans += idx_rows

        return ans


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]

solution = Solution()
print(solution.countNegatives(grid))