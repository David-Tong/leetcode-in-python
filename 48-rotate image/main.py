class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        if size == 0:
            return

        def rotateElement(matrix, left, top, width, i, j):
            temp = [0] * 4;
            temp[0] = matrix[left+i][top+j]

            for index in range(4):
                i2 = j
                j2 = width - i - 1
                if index < 3:
                    temp[index+1] = matrix[left+i2][top+j2]
                matrix[left+i2][top+j2] = temp[index]
                i = i2
                j = j2

        def rotateEdge(matrix, left, top, width):
            if width == 1:
                return
            else:
                for index in range(width-1):
                    rotateElement(matrix, left, top, width, 0, index)

        steps = size // 2
        for step in range(steps):
            rotateEdge(matrix, step, step, size-step*2)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

solution = Solution()
solution.rotate(matrix)
print(matrix)