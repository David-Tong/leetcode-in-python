class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        def getDistSum(x, y):
            from math import sqrt
            dist = 0
            for position in positions:
                dist += sqrt((x - position[0]) ** 2 + (y - position[1]) ** 2)
            return dist

        # start
        step = 1
        x, y = positions[0]
        dist = getDistSum(x, y)

        # search in super parabola plane
        while step > 10 ** -6:
            shrink = True
            DIRECTIONS = [(0, step), (0, -1 * step), (step, 0), (-1 * step, 0)]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                n_dist = getDistSum(nx, ny)
                if n_dist < dist:
                    dist = n_dist
                    x, y = nx, ny
                    shrink = False
            if shrink:
                step = step * 1.0 / 10
        return dist


positions = [[0,1],[1,0],[1,2],[2,1]]
positions = [[1,1],[3,3]]
positions = [[1,0],[5,0]]
positions = [[0,1],[1,0],[1,2],[2,1],[1,1]]

solution = Solution()
print(solution.getMinDistSum(positions))
