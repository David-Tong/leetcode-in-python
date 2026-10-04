class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        # pre-process
        X = max(towers, key=lambda x: x[0])[0] + radius
        Y = max(towers, key=lambda x: x[1])[1] + radius

        # helper function
        from math import sqrt
        def getQuality(x, y, tower):
            d = sqrt((x - tower[0]) ** 2 + (y - tower[1]) ** 2)
            if d <= radius:
                quality = int(tower[2] / (1 + d))
            else:
                quality = 0
            return quality

        def getQualities(x, y):
            qualities = 0
            for tower in towers:
                qualities += getQuality(x, y, tower)
            return qualities

        # process
        maxi = 0
        ans = (0, 0)
        for x in range(X + 1):
            for y in range(Y + 1):
                qualities = getQualities(x, y)
                if qualities > maxi:
                    maxi = qualities
                    ans = (x, y)
        return ans


towers = [[1,2,5],[2,1,7],[3,1,9]]
radius = 2

towers = [[23,11,21]]
radius = 9

towers = [[1,2,13],[2,1,7],[0,1,9]]
radius = 2

towers = [[42,0,0]]
radius = 7

"""
from random import randint
towers = [[randint(0, 50), randint(0, 50), randint(0, 50)] for _ in range(50)]
radius = 25
print(towers)
"""

solution = Solution()
print(solution.bestCoordinate(towers, radius))
