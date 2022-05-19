class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        M = len(mat)

        def rotateOnce(mat):
            matrix = [[0] * M for _ in range(M)]
            for x in range(M):
                for y in range(M):
                    matrix[y][M - 1 - x] = mat[x][y]
            return matrix

        def doEqual(matrix, target):
            for x in range(M):
                for y in range(M):
                    if matrix[x][y] != target[x][y]:
                        return False
            return True

        matrix = mat
        for x in range(4):
            if doEqual(matrix, target):
                return True
            matrix = rotateOnce(matrix)
        return False


mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]

solution = Solution()
print(solution.findRotation(mat, target))
