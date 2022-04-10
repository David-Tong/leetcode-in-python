class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        M = len(mat)
        N = len(mat[0])
        dp = [[0] * N for x in range(M)]
        for x in range(M):
            for y in range(N):
                if y == 0:
                    dp[x][y] = mat[x][y]
                else:
                    dp[x][y] = dp[x][y-1] + mat[x][y]

        answer = [[0] * N for x in range(M)]
        for x in range(M):
            for y in range(N):
                low_x = max(0, x - k)
                high_x = min(M, x + k + 1)
                for z in range(low_x, high_x):
                    low_y = y - k - 1
                    high_y = min(N - 1, y + k)
                    if low_y >= 0:
                        answer[x][y] += dp[z][high_y] - dp[z][low_y]
                    else:
                        answer[x][y] += dp[z][high_y]
        return answer


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2

mat = [[1]]
k = 100

solution = Solution()
print(solution.matrixBlockSum(mat, k))
