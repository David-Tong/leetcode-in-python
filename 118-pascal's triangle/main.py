class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = list()
        triangle.append([1])

        for row in range(1, numRows):
            level = list()
            for col in range(len(triangle[row-1]) + 1):
                item = 0
                if col > 0:
                    item += triangle[row-1][col-1]
                if col < len(triangle[row-1]):
                    item += triangle[row-1][col]
                level.append(item)
            triangle.append(level)

        return triangle


numRows = 30

solution = Solution()
print(solution.generate(numRows))
