class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])
        dx, dy = 1, 1

        bottom_lefts = list()
        for row in range(M):
            x, y = row, 0
            bottom_left = list()
            while x < M:
                bottom_left.append(grid[x][y])
                x, y = x + dx, y + dy
            bottom_lefts.append(bottom_left)

        top_rights = list()
        for col in range(1, N):
            x, y = 0, col
            top_right = list()
            while y < N:
                top_right.append(grid[x][y])
                x, y = x + dx, y + dy
            top_rights.append(top_right)

        # print(bottom_lefts)
        # print(top_rights)

        # process
        for row in range(M):
            x, y = row, 0
            bottom_left = sorted(bottom_lefts[row], reverse=True)
            idx = 0
            while x < M:
                grid[x][y] = bottom_left[idx]
                x, y = x + dx, y + dy
                idx += 1

        for col in range(1, N):
            x, y = 0, col
            top_right = sorted(top_rights[col - 1])
            idx = 0
            while y < N:
                grid[x][y] = top_right[idx]
                x, y = x + dx, y + dy
                idx += 1

        return grid


grid = [[1,7,3],[9,8,2],[4,5,6]]
grid = [[0,1],[1,2]]
grid = [[1]]

solution = Solution()
print(solution.sortMatrix(grid))
