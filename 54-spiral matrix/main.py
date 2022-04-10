class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def doSpiral(matrix, ans, left, right, top, down):
            if left < right and top < down:
                # left to right, the first row
                for x in range(left, right + 1):
                    ans.append(matrix[top][x])

                # top to down, the last column
                for y in range(top + 1, down):
                    ans.append(matrix[y][right])

                # right to left, the last row
                for x in range(right, left - 1, -1):
                    ans.append(matrix[down][x])

                # down to top, the first column
                for y in range(down - 1, top, -1):
                    ans.append(matrix[y][left])

                doSpiral(matrix, ans, left + 1, right - 1, top + 1, down - 1)

            elif left == right and top == down:
                ans.append(matrix[top][left])
            elif left == right:
                for row in range(top, down + 1):
                    ans.append(matrix[row][left])
            elif top == down:
                ans.extend(matrix[top][left:right + 1])

        ans = []
        doSpiral(matrix, ans, 0, len(matrix[0]) - 1, 0, len(matrix) - 1)

        return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1]]

solution = Solution()
print(solution.spiralOrder(matrix))
