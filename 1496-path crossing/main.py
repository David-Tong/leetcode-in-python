class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        points = list()
        point = (0, 0)
        points.append(point)

        for pth in path:
            if pth == "N":
                point = (point[0], point[1] + 1)
            elif pth == "S":
                point = (point[0], point[1] - 1)
            elif pth == "E":
                point = (point[0] + 1, point[1])
            elif pth == "W":
                point = (point[0] - 1, point[1])
            if point in points:
                return True
            points.append(point)
        return False


path = "NES"
path = "NESWW"

solution = Solution()
print(solution.isPathCrossing(path))
