class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(mat)
        N = len(mat[0])

        # sort the first column's matrix diagonal
        for x in range(M):
            # sort
            sx = x
            sy = 0
            items = list()
            while sx < M and sy < N:
                items.append(mat[sx][sy])
                sx += 1
                sy += 1
            items = sorted(items)

            # re-arrange
            sx = x
            sy = 0
            index = 0
            while sx < M and sy < N:
                mat[sx][sy] = items[index]
                sx += 1
                sy += 1
                index += 1

        # sort the first row's matrix diagonal
        for y in range(1, N):
            # sort
            sx = 0
            sy = y
            items = list()
            while sx < M and sy < N:
                items.append(mat[sx][sy])
                sx += 1
                sy += 1
            items = sorted(items)

            # re-arrange
            sx = 0
            sy = y
            index = 0
            while sx < M and sy < N:
                mat[sx][sy] = items[index]
                sx += 1
                sy += 1
                index += 1

        return mat


mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

solution = Solution()
print(solution.diagonalSort(mat))
