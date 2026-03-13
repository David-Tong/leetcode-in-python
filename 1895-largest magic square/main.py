class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(grid)
        N = len(grid[0])

        # presums for rows
        row_presums = list()
        for x in range(M):
            presum = [0]
            for y in range(N):
                presum.append(presum[-1] + grid[x][y])
            row_presums.append(presum)
        # print(row_presums)

        # presums for columns
        column_presums = list()
        for y in range(N):
            presum = [0]
            for x in range(M):
                presum.append(presum[-1] + grid[x][y])
            column_presums.append(presum)
        # print(column_presums)

        # presums for diagonals
        diagonal_presums = list()
        for y in range(N - 1, -1, -1):
            x = 0
            presum = [0]
            while 0 <= x < M and 0 <= y < N:
                presum.append(presum[-1] + grid[x][y])
                x += 1
                y += 1
            diagonal_presums.append(presum)
        for x in range(1, M):
            y = 0
            presum = [0]
            while 0 <= x < M and 0 <= y < N:
                presum.append(presum[-1] + grid[x][y])
                x += 1
                y += 1
            diagonal_presums.append(presum)
        # print(diagonal_presums)

        # presums for anti diagnoals
        anti_diagonal_presums = list()
        for y in range(N):
            x = 0
            presum = [0]
            while 0 <= x < M and 0 <= y < N:
                presum.append(presum[-1] + grid[x][y])
                x += 1
                y -= 1
            anti_diagonal_presums.append(presum)
        for x in range(1, M):
            y = N - 1
            presum = [0]
            while 0 <= x < M and 0 <= y < N:
                presum.append(presum[-1] + grid[x][y])
                x += 1
                y -= 1
            anti_diagonal_presums.append(presum)
        # print(anti_diagonal_presums)
        # print(len(anti_diagonal_presums))

        # helper function
        def getDiagonalIndex(x, y):
            return x - (y + 1) + N

        def getAntiDiagonalIndex(x, y):
            return x + y

        def getDiagonalOffset(x, y):
            return y if x >= y else x

        def getAntiDiagonalOffset(x, y):
            idx = getAntiDiagonalIndex(x, y)
            if idx >= N:
                return x - (idx - N + 1)
            else:
                return x

        def isMagic(sx, sy, k):
            # print(sx, sy, k)
            ex, ey = sx + k, sy + k
            target = row_presums[sx][ey + 1] - row_presums[sx][sy]

            # check rows sum
            for x in range(sx, ex + 1):
                if row_presums[x][ey + 1] - row_presums[x][sy] != target:
                    return False

            # check columns sum
            for y in range(sy, ey + 1):
                if column_presums[y][ex + 1] - column_presums[y][sx] != target:
                    return False

            # check diaganol
            idx = getDiagonalIndex(sx, sy)
            s_offset = getDiagonalOffset(sx, sy)
            e_offset = getDiagonalOffset(ex, ey)
            if diagonal_presums[idx][e_offset + 1] - diagonal_presums[idx][s_offset] != target:
                return False

            # check anti-diagonal
            idx = getAntiDiagonalIndex(sx, ey)
            s_offset = getAntiDiagonalOffset(sx, ey)
            e_offset = getAntiDiagonalOffset(ex, sy)
            if anti_diagonal_presums[idx][e_offset + 1] - anti_diagonal_presums[idx][s_offset] != target:
                return False

            return True

        # process
        for k in range(min(M, N) - 1, 0, -1):
            for sx in range(M):
                for sy in range(N):
                    ex, ey = sx + k, sy + k
                    if 0 <= ex < M and 0 <= ey < N:
                       if isMagic(sx, sy, k):
                            return k + 1
        return 1


grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
"""
grid = [[1] * 50 for _ in range(50)]
print(grid)
"""
grid = [[19,11,15,20,2,9,14,5],[15,5,9,3,13,1,10,2],[4,13,8,20,18,8,14,3],[14,8,2,2,12,5,10,7],[12,9,18,20,7,9,11,2],[7,17,2,8,8,13,6,16]]

solution = Solution()
print(solution.largestMagicSquare(grid))
