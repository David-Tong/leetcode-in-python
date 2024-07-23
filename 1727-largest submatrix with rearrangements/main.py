class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(matrix)
        N = len(matrix[0])

        for x in range(1, M):
            for y in range(N):
                if matrix[x][y] == 1:
                    matrix[x][y] += matrix[x - 1][y]

        # process
        ans = 0
        for x in range(M):
            row = sorted(matrix[x][:], reverse=True)
            for y in range(N):
                if row[y] == 0:
                    break
                ans = max(ans, row[y] * (y + 1))
        return ans


matrix = [[0,0,1],[1,1,1],[1,0,1]]
matrix = [[1,0,1,0,1]]
matrix = [[1,1,0],[1,0,1]]

solution = Solution()
print(solution.largestSubmatrix(matrix))
