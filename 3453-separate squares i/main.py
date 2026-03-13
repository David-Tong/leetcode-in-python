class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # pre-process
        TARGET = sum([x[2] ** 2 for x in squares]) * 1.0 / 2
        LIMIT = max([x[1] + x[2] for x in squares])
        # print(TARGET)

        def sumArea(target):
            area = 0
            for square in squares:
                x, y, l = square
                if y > target:
                    pass
                elif y + l < target:
                    area += l ** 2
                else:
                    area += (target - y) * 1.0 / l * (l ** 2)
            return area

        # process
        # binary search
        left, right = 0, LIMIT
        DELTA = 10 ** -5
        while left + DELTA < right:
            middle = ((left + right) * 1.0) / 2
            target = sumArea(middle)
            if target < TARGET:
                left = middle
            elif target >= TARGET:
                right = middle
        return left


squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]
from random import randint
squares = [[randint(0, 10000), randint(0, 10000), randint(1, 100)] for _ in range(5 * 10 ** 4)]
print(squares)

solution = Solution()
print(solution.separateSquares(squares))
