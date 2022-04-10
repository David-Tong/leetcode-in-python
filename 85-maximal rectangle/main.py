class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for x in range(M)]
        prefix = [[0] * N for x in range(M)]

        for x in range(M):
            for y in range(N):
                if matrix[x][y] == "0":
                    prefix[x][y] = 0
                else:
                    if y > 0:
                        prefix[x][y] = prefix[x][y - 1] + int(matrix[x][y])
                    else:
                        prefix[x][y] = int(matrix[x][y])

        for x in range(M):
            for y in range(N):
                if prefix[x][y] > 0:
                    width = float("inf")
                    if x > 0:
                        for z in range(0, x + 1):
                            width = min(width, prefix[x - z][y])
                            if width == 0:
                                break
                            dp[x][y] = max(dp[x][y], width * (z + 1))
                    else:
                        dp[x][y] = prefix[x][y]

        ans = 0
        for x in range(M):
            ans = max(ans, max(dp[x]))
        return ans


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#matrix = [["1","0","1","1","1"],["1","0","1","1","1"],["1","1","0","1","1"],["1","0","0","1","1"]]
#matrix = [["0"]]
#matrix = [["1"]]
matrix = [["0","0","1"],["1","1","1"]]
matrix=[["0","0","0","0","0","0","1"],["0","0","0","0","1","1","1"],["1","1","1","1","1","1","1"],["0","0","0","1","1","1","1"]]

solution = Solution()
print(solution.maximalRectangle(matrix))
