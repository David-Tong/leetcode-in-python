class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(mat)
        N = len(mat[0])

        rows = list()
        for row in mat:
            rows.append(sum(row))

        columns = list()
        for y in range(N):
            column = 0
            for x in range(M):
                column += mat[x][y]
            columns.append(column)

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                if rows[x] == 1 and columns[y] == 1:
                    if mat[x][y] == 1:
                        ans += 1
        return ans


mat = [[1,0,0],[0,0,1],[1,0,0]]
mat = [[1,0,0],[0,1,0],[0,0,1]]
mat = [[1]]

solution = Solution()
print(solution.numSpecial(mat))
