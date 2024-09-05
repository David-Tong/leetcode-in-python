class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x_left = x_center - radius
        self.x_right = x_center + radius
        self.y_bottom = y_center - radius
        self.y_top = y_center + radius

    def randPoint(self):
        """
        :rtype: List[float]
        """
        from random import uniform
        while True:
            x = uniform(self.x_left, self.x_right)
            y = uniform(self.y_bottom, self.y_top)
            z = (x - self.x_center) ** 2 + (y - self.y_center) ** 2

            if z <= self.radius ** 2:
                return [x, y]


solution = Solution(1.0, 0.0, 0.0)
solution = Solution(0.01, -73839.1, -3289891.3)
for x in range(100):
    print(solution.randPoint())
