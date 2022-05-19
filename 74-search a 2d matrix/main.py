class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if matrix[middle][0] > target:
                right = middle
            elif matrix[middle][0] < target:
                left = middle
            else:
                return True

        row = 0
        if matrix[right][0] < target:
            row = right
        elif matrix[right][0] == target:
            return True
        else:
            if matrix[left][0] < target:
                row = left
            elif matrix[left][0] == target:
                return True
            else:
                return False

        left = 0
        right = len(matrix[0]) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if matrix[row][middle] > target:
                right = middle
            elif matrix[row][middle] < target:
                left =middle
            else:
                return True

        if matrix[row][left] == target:
            return True
        elif matrix[row][right] == target:
            return True
        else:
            return False