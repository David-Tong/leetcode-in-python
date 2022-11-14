class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M = len(matrix)
        N = len(matrix[0])

        for x in range(M - 1, -1, -1):
            y = 0
            while 0 <= x + 1 < M and 0 <= y + 1 < N:
                if matrix[x][y] != matrix[x + 1][y + 1]:
                    return False
                else:
                    x += 1
                    y += 1

        for y in range(1, N, 1):
            x = 0
            while 0 <= x + 1 < M and 0 <= y + 1 < N:
                if matrix[x][y] != matrix[x + 1][y + 1]:
                    return False
                else:
                    x += 1
                    y += 1

        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
matrix = [[1]]

solution = Solution()
print(solution.isToeplitzMatrix(matrix))
