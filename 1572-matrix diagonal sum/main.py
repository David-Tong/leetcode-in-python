class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        N = len(mat)
        ans = 0
        for x in range(N):
            ans += mat[x][x]

        for x in range(N):
            ans += mat[x][N-x-1]

        if N % 2 == 1:
            m = N // 2
            ans -= mat[m][m]

        return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

solution = Solution()
print(solution.diagonalSum(mat))