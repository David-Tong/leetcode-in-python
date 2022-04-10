class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        mr = len(mat)
        mc = len(mat[0])

        if mr * mc != r * c:
            return mat

        if mr == r and mc == c:
            return mat

        matrix = []
        row = []
        index = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if index > 0 and index % c == 0:
                    matrix.append(row)
                    row = []
                index += 1
                row.append(mat[i][j])

        matrix.append(row)
        return matrix


mat = [[1,2],[3,4]]
r = 1
c = 4

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r = 6
c = 2

solution = Solution()
print(solution.matrixReshape(mat, r, c))
