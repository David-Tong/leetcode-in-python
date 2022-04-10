class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def doMatrix(left, top, matrix, start, step):
            if step > 0:
                if step == 1:
                    matrix[left][top] = start
                else:
                    for x in range(left, left + step):
                        matrix[top][x] = start
                        start += 1

                    for y in range(top + 1, top + step - 1):
                        matrix[y][left + step - 1] = start
                        start += 1

                    for x in range(left + step - 1, left - 1, -1):
                        matrix[top + step - 1][x] = start
                        start += 1

                    for y in range(top + step - 2, top, -1):
                        matrix[y][left] = start
                        start += 1
                    doMatrix(left + 1, top + 1, matrix, start, step - 2)

        matrix = [[0] * n for _ in range(n)]
        doMatrix(0, 0, matrix, 1, n)
        return matrix


n = 3
n = 1
n = 4
n = 5
n = 20

solution = Solution()
print(solution.generateMatrix(n))
