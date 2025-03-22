class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # pre-process
        # find closest point on rectangle to circle
        cx = max(x1, min(x2, xCenter))
        cy = max(y1, min(y2, yCenter))

        # process
        distance = (cx - xCenter) ** 2 + (cy - yCenter) ** 2
        if distance > radius ** 2:
            return False
        else:
            return True


radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1

solution = Solution()
print(solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
