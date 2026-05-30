class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # row presum
        row_presum = [0]
        for x in range(M):
            row = 0
            for y in range(N):
                row += grid[x][y]
            row_presum.append(row_presum[-1] + row)
        # print(row_presum)

        # column presum
        column_presum = [0]
        for y in range(N):
            column = 0
            for x in range(M):
                column += grid[x][y]
            column_presum.append(column_presum[-1] + column)
        # print(column_presum)

        # process
        # check row sum
        for x in range(M):
            if row_presum[M] == 2 * row_presum[x]:
                return True

        # check column sum
        for y in range(N):
            if column_presum[N] == 2 * column_presum[y]:
                return True

        return False


grid = [[1,4],[2,3]]
grid = [[1,3],[2,4]]
grid = [[28443],[33959]]

solution = Solution()
print(solution.canPartitionGrid(grid))
