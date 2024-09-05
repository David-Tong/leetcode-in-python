class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        # x - number of jumbo burger
        # y - number of small burger
        # quadratic system of equations
        #     4 * x + 2 * y = tomatoSlices
        #     x + y = cheeseSlices
        #     4 * x + 2 (cheeseSlices - x) = tomatoSlices
        #         x = (tomatoSlices - cheeseSlices * 2 ) / 2
        #         y = cheesesSlices - x
        if (tomatoSlices - cheeseSlices * 2) % 2 == 0:
            x = (tomatoSlices - cheeseSlices * 2) / 2
            if x >= 0:
                y = cheeseSlices - x
                if y >= 0:
                    return [x, y]

        return []


tomatoSlices = 16
cheeseSlices = 7

tomatoSlices = 17
cheeseSlices = 4

tomatoSlices = 4
cheeseSlices = 17

tomatoSlices = 0
cheeseSlices = 0

solution = Solution()
print(solution.numOfBurgers(tomatoSlices, cheeseSlices))
