class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(matrix)
        N = len(matrix[0])
        ans = [[0] * M for _ in range(N)]
        for x in range(M):
            for y in range(N):
                ans[y][x] = matrix[x][y]
        return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
matrix = [[1]]

solution = Solution()
print(solution.transpose(matrix))
