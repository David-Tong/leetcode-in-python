class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        rowbits = 0
        colbits = 0
        for x in range(M):
            product = 1
            for y in range(N):
                product *= matrix[x][y]
            if product == 0:
                rowbits |= 1 << x

        for y in range(N):
            product = 1
            for x in range(M):
                product *= matrix[x][y]
            if product == 0:
                colbits |= 1 << y

        for x in range(M):
            if (rowbits >> x) & 1 == 1:
                for y in range(N):
                    matrix[x][y] = 0

        for y in range(N):
            if (colbits >> y) & 1 == 1:
                for x in range(M):
                    matrix[x][y] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

solution = Solution()
solution.setZeroes(matrix)

print(matrix)
