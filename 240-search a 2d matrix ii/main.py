class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in range(len(matrix)):
            if matrix[row][0] <= target:
                left = 0
                right = len(matrix[0]) - 1
                while left + 1 < right:
                    middle = (left + right) // 2
                    if matrix[row][middle] < target:
                        left = middle + 1
                    elif matrix[row][middle] > target:
                        right = middle - 1
                    else:
                        return True
                if matrix[row][left] == target or matrix[row][right] == target:
                    return True
            else:
                return False
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

matrix = [[1]]
target = 1

solution = Solution()
print(solution.searchMatrix(matrix, target))
