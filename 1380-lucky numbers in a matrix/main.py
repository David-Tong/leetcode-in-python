class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        M = len(matrix)
        N = len(matrix[0])
        minis = list()
        for row in matrix:
            minis.append(min(row))
        maxis = list()
        for y in range(N):
            maxi = float("-inf")
            for x in range(M):
                maxi = max(maxi, matrix[x][y])
            maxis.append(maxi)

        # process
        ans = list()
        for x in range(M):
            for y in range(N):
                if matrix[x][y] == minis[x] and matrix[x][y] == maxis[y]:
                    ans.append(matrix[x][y])
        return ans


matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
matrix = [[7,8],[1,2]]

solution = Solution()
print(solution.luckyNumbers(matrix))
