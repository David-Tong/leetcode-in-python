class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(matrix)
        N = len(matrix[0])

        for x in range(1, M):
            for y in range(1, N):
                if matrix[x][y] == 1:
                    matrix[x][y] = min(matrix[x - 1][y - 1], matrix[x - 1][y], matrix[x][y - 1]) + 1
        # print(matrix)

        # process
        ans = 0
        for x in range(M):
            for y in range(N):
                ans += matrix[x][y]
        return ans

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

matrix = [
    [1]
]

matrix = [
    [1,1,1,1]
]

matrix = [
    [1],
    [1],
    [1]
]


solution = Solution()
print(solution.countSquares(matrix))
