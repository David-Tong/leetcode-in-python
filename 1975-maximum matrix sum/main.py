class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # pre-process
        M = len(matrix)
        N = len(matrix[0])

        # process
        zeros, negatives = 0, 0
        maxi = float("inf")
        total = 0
        for x in range(M):
            for y in range(N):
                total += abs(matrix[x][y])
                maxi = min(maxi, abs(matrix[x][y]))
                if matrix[x][y] < 0:
                    negatives += 1

        # post-process
        if negatives % 2 == 1:
            ans = total - 2 * maxi
        else:
            ans = total
        return ans


matrix = [[1,-1],[-1,1]]
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
matrix = [[-1,-2,-3],[-6,2,7],[-2,-2,-3]]
matrix = [[-1,0,-1],[-2,1,3],[3,2,2]]
matrix = [[-1,0,-1],[-2,1,3],[3,2,0]]
matrix = [[-1,0,-1],[-2,1,3],[3,0,0]]
matrix = [[2,9,3],[5,4,-4],[1,7,1]]

solution = Solution()
print(solution.maxMatrixSum(matrix))
